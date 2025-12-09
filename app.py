"""
Marketing Analytics Dashboard - Streamlit Web Application
Deploy this app to make the dashboard visible online
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
import sys

# Page configuration
st.set_page_config(
    page_title="Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load dashboard metrics data"""
    try:
        # Try to load processed metrics
        import os
        metrics_path = 'data/processed/dashboard_metrics.csv'
        
        # Check if file exists
        if not os.path.exists(metrics_path):
            st.error(f"Data file not found: {metrics_path}")
            st.info("Please ensure data files are in the repository.")
            return None, None
            
        metrics_df = pd.read_csv(metrics_path)
        
        # Try to load raw GA data
        ga_path = 'data/raw/ga_export.csv'
        ga_df = None
        if os.path.exists(ga_path):
            try:
                ga_df = pd.read_csv(ga_path)
            except Exception as e:
                st.warning(f"Could not load GA data: {str(e)}")
                ga_df = None
            
        return metrics_df, ga_df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        import traceback
        st.code(traceback.format_exc())
        return None, None

def calculate_kpi_summary(metrics_df):
    """Calculate summary KPIs from metrics data"""
    if metrics_df is None or len(metrics_df) == 0:
        return {}
    
    summary = {}
    
    # Extract numeric values (remove % and convert)
    def extract_value(val):
        if isinstance(val, str):
            val = val.replace('%', '').replace(',', '')
        try:
            return float(val)
        except:
            return 0
    
    # Calculate overall metrics
    overall = metrics_df[metrics_df['Channel'] == 'Overall']
    if len(overall) > 0:
        roas_row = overall[overall['KPI'] == 'ROAS']
        revenue_row = overall[overall['KPI'] == 'Total Revenue']
        cost_row = overall[overall['KPI'] == 'Total Cost']
        
        if len(roas_row) > 0:
            summary['ROAS'] = extract_value(roas_row.iloc[0]['Value'])
        if len(revenue_row) > 0:
            summary['Total Revenue'] = extract_value(revenue_row.iloc[0]['Value'])
        if len(cost_row) > 0:
            summary['Total Cost'] = extract_value(cost_row.iloc[0]['Value'])
    
    # Calculate channel-specific metrics
    google_ads = metrics_df[metrics_df['Channel'] == 'Google Ads']
    facebook = metrics_df[metrics_df['Channel'] == 'Facebook']
    organic = metrics_df[metrics_df['Channel'] == 'Organic']
    email = metrics_df[metrics_df['Channel'] == 'Email']
    
    if len(google_ads) > 0:
        clicks_row = google_ads[google_ads['KPI'] == 'Clicks']
        conversions_row = google_ads[google_ads['KPI'] == 'Conversions']
        if len(clicks_row) > 0:
            summary['Google Ads Clicks'] = extract_value(clicks_row.iloc[0]['Value'])
        if len(conversions_row) > 0:
            summary['Google Ads Conversions'] = extract_value(conversions_row.iloc[0]['Value'])
    
    if len(facebook) > 0:
        clicks_row = facebook[facebook['KPI'] == 'Clicks']
        if len(clicks_row) > 0:
            summary['Facebook Clicks'] = extract_value(clicks_row.iloc[0]['Value'])
    
    if len(organic) > 0:
        sessions_row = organic[organic['KPI'] == 'Sessions']
        if len(sessions_row) > 0:
            summary['Organic Sessions'] = extract_value(sessions_row.iloc[0]['Value'])
    
    return summary

def main():
    # Header
    st.markdown('<h1 class="main-header">📊 Marketing Analytics Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    metrics_df, ga_df = load_data()
    
    if metrics_df is None or len(metrics_df) == 0:
        st.error("Unable to load dashboard data. Please ensure data files are available.")
        st.info("""
        **Troubleshooting:**
        1. Ensure `data/processed/dashboard_metrics.csv` exists in the repository
        2. Check that the file path is correct
        3. Verify the file is committed to GitHub
        """)
        return
    
    # Calculate summary KPIs
    kpi_summary = calculate_kpi_summary(metrics_df)
    
    # Sidebar filters
    st.sidebar.header("📅 Filters")
    
    # Date filter
    if 'Date' in metrics_df.columns and len(metrics_df['Date'].unique()) > 0:
        dates = sorted(metrics_df['Date'].unique(), reverse=True)
        if len(dates) > 0:
            selected_date = st.sidebar.selectbox("Select Date", dates, index=0)
            filtered_df = metrics_df[metrics_df['Date'] == selected_date]
        else:
            filtered_df = metrics_df
    else:
        filtered_df = metrics_df
    
    # Channel filter
    unique_channels = metrics_df['Channel'].unique().tolist() if 'Channel' in metrics_df.columns else []
    if len(unique_channels) > 0:
        channels = ['All'] + unique_channels
        selected_channel = st.sidebar.selectbox("Select Channel", channels)
        if selected_channel != 'All':
            filtered_df = filtered_df[filtered_df['Channel'] == selected_channel]
    else:
        st.warning("No channel data available.")
    
    # Main dashboard
    st.markdown("---")
    
    # KPI Cards Row 1
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        roas = kpi_summary.get('ROAS', 0)
        delta_value = None
        if roas > 0 and 3.50 > 0:
            delta_value = f"{((roas - 3.50) / 3.50 * 100):.1f}%"
        st.metric(
            label="📈 ROAS",
            value=f"{roas:.2f}",
            delta=delta_value
        )
    
    with col2:
        revenue = kpi_summary.get('Total Revenue', 0)
        st.metric(
            label="💰 Total Revenue",
            value=f"${revenue:,.0f}" if revenue > 0 else "$0",
            delta=f"${revenue - 150000:,.0f}" if revenue > 150000 else None
        )
    
    with col3:
        cost = kpi_summary.get('Total Cost', 0)
        st.metric(
            label="💵 Total Cost",
            value=f"${cost:,.0f}" if cost > 0 else "$0",
            delta=f"${cost - 45000:,.0f}" if cost < 45000 else None,
            delta_color="inverse"
        )
    
    with col4:
        clicks = kpi_summary.get('Google Ads Clicks', 0) + kpi_summary.get('Facebook Clicks', 0)
        st.metric(
            label="🖱️ Total Clicks",
            value=f"{clicks:,.0f}" if clicks > 0 else "0"
        )
    
    st.markdown("---")
    
    # Charts Row
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Performance by Channel")
        
        # Prepare data for channel comparison
        channel_data = []
        for channel in metrics_df['Channel'].unique():
            channel_df = metrics_df[metrics_df['Channel'] == channel]
            if 'Clicks' in channel_df['KPI'].values:
                clicks_row = channel_df[channel_df['KPI'] == 'Clicks']
                if len(clicks_row) > 0:
                    clicks_val = clicks_row.iloc[0]['Value']
                    clicks_val = float(str(clicks_val).replace(',', '').replace('%', ''))
                    channel_data.append({'Channel': channel, 'Clicks': clicks_val})
        
        if channel_data:
            channel_df_plot = pd.DataFrame(channel_data)
            fig = px.bar(
                channel_df_plot,
                x='Channel',
                y='Clicks',
                color='Channel',
                title="Clicks by Channel",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No channel click data available to display.")
    
    with col2:
        st.subheader("🎯 KPI Performance")
        
        # Create KPI comparison chart
        kpi_data = []
        for _, row in filtered_df.iterrows():
            try:
                value = str(row['Value']).replace('%', '').replace(',', '')
                target = str(row['Target']).replace('%', '').replace(',', '')
                kpi_data.append({
                    'KPI': row['KPI'],
                    'Value': float(value),
                    'Target': float(target),
                    'Channel': row['Channel']
                })
            except:
                continue
        
        if kpi_data:
            kpi_df_plot = pd.DataFrame(kpi_data)
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=kpi_df_plot['KPI'],
                y=kpi_df_plot['Value'],
                name='Actual',
                marker_color='#1f77b4'
            ))
            fig.add_trace(go.Bar(
                x=kpi_df_plot['KPI'],
                y=kpi_df_plot['Target'],
                name='Target',
                marker_color='#ff7f0e'
            ))
            fig.update_layout(
                title="Actual vs Target KPIs",
                xaxis_title="KPI",
                yaxis_title="Value",
                barmode='group',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No KPI data available to display.")
    
    # Data Table
    st.markdown("---")
    st.subheader("📋 Detailed Metrics")
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 1rem;'>
            <p>Marketing Analytics Dashboard | Last Updated: {}</p>
            <p>Automated KPI tracking with 25+ real-time metrics</p>
        </div>
        """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.exception(e)
        st.info("""
        **If you're seeing this error:**
        1. Check that all data files are in the repository
        2. Verify requirements.txt includes all dependencies
        3. Check Streamlit Cloud logs for more details
        """)

