import pandas as pd
import numpy as np
from google.oauth2.service_account import Credentials
from google.cloud import bigquery
import gspread
import schedule
import time
from datetime import datetime, timedelta

class MarketingDashboardAutomation:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.bq_client = None
        self.gs_client = None
        
    def initialize_clients(self):
        """Initialize BigQuery and Google Sheets clients"""
        credentials = Credentials.from_service_account_file(self.config_path)
        self.bq_client = bigquery.Client(credentials=credentials)
        self.gs_client = gspread.authorize(credentials)
        print("Clients initialized successfully")
        
    def fetch_ga4_data(self):
        """Fetch Google Analytics 4 data from BigQuery"""
        query = """
        SELECT 
            DATE(event_timestamp) as date,
            COUNT(DISTINCT user_id) as users,
            COUNT(*) as sessions,
            ROUND(AVG(session_duration), 2) as avg_session_duration,
            ROUND(COUNT(CASE WHEN event_name='purchase' THEN 1 END)/COUNT(*)*100, 2) as conversion_rate
        FROM `project.dataset.events_*`
        WHERE DATE(event_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        GROUP BY date
        ORDER BY date DESC
        """
        df = self.bq_client.query(query).to_dataframe()
        print(f"Fetched {len(df)} days of GA4 data")
        return df
    
    def fetch_ads_data(self):
        """Fetch Google Ads performance data"""
        query = """
        SELECT
            DATE(event_date) as date,
            campaign_name,
            SUM(impressions) as impressions,
            SUM(clicks) as clicks,
            SUM(cost) as cost,
            SUM(conversions) as conversions,
            ROUND(SUM(cost)/SUM(conversions), 2) as cpa
        FROM `project.dataset.google_ads`
        WHERE DATE(event_date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        GROUP BY date, campaign_name
        ORDER BY date DESC
        """
        df = self.bq_client.query(query).to_dataframe()
        print(f"Fetched Ads data for {df['campaign_name'].nunique()} campaigns")
        return df
    
    def calculate_kpis(self, ga_data, ads_data):
        """Calculate marketing KPIs"""
        kpis = {
            'total_users': ga_data['users'].sum(),
            'total_sessions': ga_data['sessions'].sum(),
            'avg_conversion_rate': ga_data['conversion_rate'].mean(),
            'avg_cpa': ads_data['cpa'].mean() if len(ads_data) > 0 else 0,
            'total_spend': ads_data['cost'].sum() if len(ads_data) > 0 else 0,
            'roas': (ads_data['conversions'].sum() * 100) / ads_data['cost'].sum() if ads_data['cost'].sum() > 0 else 0
        }
        print(f"\nCalculated KPIs:")
        for key, value in kpis.items():
            print(f"  {key}: {value}")
        return kpis
    
    def update_dashboard(self, ga_data, ads_data, kpis):
        """Update Google Sheets dashboard with metrics"""
        try:
            spreadsheet = self.gs_client.open('Marketing Analytics Dashboard')
            worksheet = spreadsheet.worksheet('KPIs')
            
            # Update KPIs
            worksheet.update('B2', kpis['total_users'])
            worksheet.update('B3', kpis['total_sessions'])
            worksheet.update('B4', round(kpis['avg_conversion_rate'], 2))
            worksheet.update('B5', round(kpis['avg_cpa'], 2))
            worksheet.update('B6', round(kpis['total_spend'], 2))
            worksheet.update('B7', round(kpis['roas'], 2))
            
            print("Dashboard updated successfully")
            return True
        except Exception as e:
            print(f"Error updating dashboard: {str(e)}")
            return False
    
    def run_pipeline(self):
        """Run complete dashboard automation pipeline"""
        print("\n" + "="*50)
        print("Starting Marketing Analytics Dashboard Update")
        print(f"Timestamp: {datetime.now()}")
        print("="*50 + "\n")
        
        try:
            self.initialize_clients()
            ga_data = self.fetch_ga4_data()
            ads_data = self.fetch_ads_data()
            kpis = self.calculate_kpis(ga_data, ads_data)
            self.update_dashboard(ga_data, ads_data, kpis)
            print("\nPipeline execution completed successfully")
        except Exception as e:
            print(f"Pipeline error: {str(e)}")
    
    def schedule_daily_updates(self):
        """Schedule daily dashboard updates"""
        schedule.every().day.at("06:00").do(self.run_pipeline)
        print("Daily updates scheduled for 06:00 UTC")
        
        while True:
            schedule.run_pending()
            time.sleep(60)


if __name__ == '__main__':
    dashboard = MarketingDashboardAutomation()
    dashboard.run_pipeline()
    # Uncomment below for scheduled updates
    # dashboard.schedule_daily_updates()
