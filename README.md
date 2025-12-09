# Marketing Analytics Dashboard - Automated KPI Tracking

Automated KPI dashboard with 25+ real-time metrics. Tracks marketing performance across Google Analytics, Google Ads, Facebook/Instagram, and Salesforce CRM.

![KPIs](https://img.shields.io/badge/KPIs-25%2B%20Metrics-blueviolet?style=flat-square&logo=googleanalytics) ![ROAS](https://img.shields.io/badge/ROAS-3.75%25-success?style=flat-square) ![Adoption](https://img.shields.io/badge/Adoption-85%25-brightgreen?style=flat-square)

## Project Overview

Automated real-time marketing performance dashboard integrating multiple data sources (Google Analytics, Google Ads, Facebook, Instagram, Salesforce CRM). Provides comprehensive KPI tracking and business insights.

This repository contains the Marketing Analytics Dashboard project that was previously part of the data-science-analytics-projects collection.

## Key Features

- **25+ KPIs**: Real-time tracking of key performance indicators
- **Multi-level Drill-down**: Analyze data by date, channel, campaign, audience
- **Real-time Updates**: Automated daily data refresh via Apache Airflow
- **Cross-platform Integration**: GA4, Google Ads, Social Media, CRM data
- **Data Sources**: Google Analytics 4, Google Ads, Facebook/Instagram, Salesforce CRM
- **ROAS Improvement**: 25%
- **CPA Reduction**: 18%
- **Adoption Rate**: 85% stakeholder adoption

## Data Sources

1. **Google Analytics 4** - Website traffic and user behavior
2. **Google Ads** - PPC performance and spend metrics
3. **Facebook/Instagram** - Social media campaign performance
4. **Salesforce CRM** - Sales pipeline and revenue data

## Key Metrics Tracked

- **Traffic Metrics**: Sessions, Users, Bounce Rate, Session Duration
- **Conversion Metrics**: Conversion Rate, Cost Per Acquisition (CPA), ROAS
- **Revenue Metrics**: Total Revenue, Average Order Value, Customer Lifetime Value
- **Ad Performance**: Impressions, Clicks, CTR, Cost Per Click (CPC)
- **Audience Metrics**: Segment Performance, User Demographics, Device Analytics
- And 19+ more KPIs

## Business Impact

- **Time Savings**: 40% reduction in manual reporting
- **ROAS Improvement**: 25% increase in return on ad spend
- **CPA Optimization**: 18% reduction in cost per acquisition
- **Stakeholder Adoption**: 85% adoption rate among team members
- **$500K+ identified** revenue opportunities

## Technical Architecture

- **Backend**: Python with Google Sheets API
- **Web Dashboard**: Streamlit for interactive web visualization
- **Orchestration**: Apache Airflow for automation
- **Data Warehouse**: BigQuery for data aggregation
- **Visualization**: Streamlit (web) + Tableau (enterprise)
- **Deployment**: Multiple platform options (Streamlit Cloud, Heroku, GCP, AWS)
- **Scheduling**: Google Cloud Scheduler / Apache Airflow

## Technologies

- Python
- Google Sheets API
- Tableau
- Apache Airflow
- BigQuery
- Google Cloud Scheduler

## Dashboard Sections

1. **Executive Summary** - Top-level KPIs and trends
2. **Traffic Analysis** - Source, device, and geo performance
3. **Conversion Funnel** - Step-by-step user journey analysis
4. **Ad Performance** - Campaign-level metrics and ROI
5. **Audience Insights** - Segmentation and behavior analysis
6. **Revenue Tracking** - Sales pipeline and revenue forecasting

## Architecture

- Data integration from multiple sources
- Real-time metric calculations
- Multi-level drill-down analysis
- Automated scheduling and updates

## Setup & Usage

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iNSRawat/marketing-analytics-dashboard.git
   cd marketing-analytics-dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the automation script**:
   ```bash
   python dashboard_automation.py
   ```

4. **Run the web dashboard locally**:
   ```bash
   streamlit run app.py
   ```
   The dashboard will be available at `http://localhost:8501`

5. **Open Jupyter Notebook for interactive analysis**:
   ```bash
   jupyter notebook Marketing_Analytics_Dashboard.ipynb
   ```
   Or use JupyterLab:
   ```bash
   jupyter lab
   ```

### Deploy Dashboard Online

The dashboard can be deployed to make it visible online. See **[DEPLOYMENT.md](DEPLOYMENT.md)** for detailed deployment instructions.

**Quick Deploy Options**:
- **Streamlit Cloud** (Recommended - Free): [Deploy Guide](DEPLOYMENT.md#option-1-streamlit-cloud-easiest--free--recommended)
- **Heroku**: [Deploy Guide](DEPLOYMENT.md#option-2-heroku-free-tier-available)
- **Google Cloud Run**: [Deploy Guide](DEPLOYMENT.md#option-3-google-cloud-run-pay-as-you-go)
- **Other Platforms**: See [DEPLOYMENT.md](DEPLOYMENT.md) for more options

## Files Included

- `app.py` - **Streamlit web dashboard application** (deploy this for online access)
- `Marketing_Analytics_Dashboard.ipynb` - **Jupyter notebook for interactive analysis** (comprehensive visualizations and insights)
- `dashboard_automation.py` - Main automation script for data updates
- `data/raw/ga_export.csv` - Google Analytics export
- `data/processed/dashboard_metrics.csv` - Processed metrics
- `requirements.txt` - Python dependencies
- `DEPLOYMENT.md` - Comprehensive deployment guide

## Dependencies

- pandas
- numpy
- streamlit (for web dashboard)
- plotly (for interactive charts)
- matplotlib & seaborn (for visualizations)
- jupyter (for notebook analysis)
- google-auth
- google-cloud-bigquery
- gspread
- schedule

Install dependencies:
```bash
pip install -r requirements.txt
```

## Analysis Options

### Option 1: Web Dashboard (Streamlit)
- **File**: `app.py`
- **Best for**: Online deployment, sharing with stakeholders
- **Run**: `streamlit run app.py`

### Option 2: Jupyter Notebook
- **File**: `Marketing_Analytics_Dashboard.ipynb`
- **Best for**: Interactive analysis, data exploration, detailed visualizations
- **Run**: `jupyter notebook Marketing_Analytics_Dashboard.ipynb`
- **Features**:
  - Comprehensive data analysis
  - Multiple visualization types (matplotlib, plotly, seaborn)
  - KPI calculations and insights
  - Channel performance comparisons
  - Time series analysis
  - Exportable reports

## 📚 Resources & Data Sources

**Project 3: Marketing Analytics Dashboard**
- **Primary Sources:**
  - [Google Analytics 4](https://marketingplatform.google.com/about/analytics/)
  - [Google Ads API](https://developers.google.com/google-ads/api)
  - [Facebook Graph API](https://developers.facebook.com/docs/graph-api)
  - [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm)
- **Dataset:** Custom marketing performance data from multiple platforms
- **Data Aggregation:** Real-time API connections to Google Marketing Platform, Google Ads, and Salesforce CRM
- **License:** MIT

## Author

Nagendra Singh Rawat | Data Science & Analytics Professional

## License

MIT
