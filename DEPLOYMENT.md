# Deployment Guide - Marketing Analytics Dashboard

This guide provides step-by-step instructions for deploying the Marketing Analytics Dashboard to various platforms where it will be publicly visible.

## 🚀 Quick Start - Recommended Platforms

### Option 1: Streamlit Cloud (Easiest & Free) ⭐ RECOMMENDED

**Best for**: Quick deployment, free hosting, automatic updates from GitHub

#### Steps:
1. **Push your code to GitHub** (already done ✅)
2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
3. **Sign in with your GitHub account**
4. **Click "New app"**
5. **Select your repository**: `iNSRawat/marketing-analytics-dashboard`
6. **Configure**:
   - **Main file path**: `app.py`
   - **Python version**: 3.9 or higher
   - **Branch**: `main`
7. **Click "Deploy"**
8. **Your dashboard will be live at**: `https://your-app-name.streamlit.app`

**Advantages**:
- ✅ Free forever
- ✅ Automatic deployments on git push
- ✅ No server management
- ✅ Built-in authentication options
- ✅ Custom domain support

---

### Option 2: Heroku (Free Tier Available)

**Best for**: Full control, add-ons, custom domains

#### Steps:

1. **Install Heroku CLI**: [Download here](https://devcenter.heroku.com/articles/heroku-cli)

2. **Create `Procfile`** (already created ✅):
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Create `setup.sh`** (already created ✅)

4. **Login to Heroku**:
   ```bash
   heroku login
   ```

5. **Create Heroku app**:
   ```bash
   heroku create marketing-dashboard-app
   ```

6. **Deploy**:
   ```bash
   git push heroku main
   ```

7. **Open your app**:
   ```bash
   heroku open
   ```

**Advantages**:
- ✅ Free tier available
- ✅ Easy scaling
- ✅ Add-ons marketplace
- ✅ Custom domains

---

### Option 3: Google Cloud Run (Pay-as-you-go)

**Best for**: Google Cloud users, serverless architecture

#### Steps:

1. **Install Google Cloud SDK**: [Install here](https://cloud.google.com/sdk/docs/install)

2. **Create `Dockerfile`** (already created ✅)

3. **Build and deploy**:
   ```bash
   # Set your project ID
   gcloud config set project YOUR_PROJECT_ID
   
   # Build the container
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/marketing-dashboard
   
   # Deploy to Cloud Run
   gcloud run deploy marketing-dashboard \
     --image gcr.io/YOUR_PROJECT_ID/marketing-dashboard \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

4. **Your dashboard will be live at**: `https://marketing-dashboard-xxxxx.run.app`

**Advantages**:
- ✅ Pay only for what you use
- ✅ Auto-scaling
- ✅ Integrated with Google Cloud services
- ✅ Free tier: 2 million requests/month

---

### Option 4: AWS Elastic Beanstalk

**Best for**: AWS ecosystem integration

#### Steps:

1. **Install AWS CLI and EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**:
   ```bash
   eb init -p python-3.9 marketing-dashboard
   ```

3. **Create environment**:
   ```bash
   eb create marketing-dashboard-env
   ```

4. **Deploy**:
   ```bash
   eb deploy
   ```

5. **Open**:
   ```bash
   eb open
   ```

---

### Option 5: DigitalOcean App Platform

**Best for**: Simple deployment, good pricing

#### Steps:

1. **Go to [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform)**

2. **Connect your GitHub repository**

3. **Configure**:
   - **Type**: Web Service
   - **Run Command**: `streamlit run app.py --server.port=8080 --server.address=0.0.0.0`
   - **Build Command**: `pip install -r requirements.txt`

4. **Deploy**

**Advantages**:
- ✅ Simple interface
- ✅ Automatic HTTPS
- ✅ $5/month starter plan

---

### Option 6: Railway (Modern Alternative)

**Best for**: Modern platform, easy setup

#### Steps:

1. **Go to [Railway](https://railway.app)**

2. **Sign in with GitHub**

3. **New Project → Deploy from GitHub**

4. **Select your repository**

5. **Configure**:
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

6. **Deploy**

**Advantages**:
- ✅ $5 free credit monthly
- ✅ Automatic deployments
- ✅ Simple interface

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure:

- [x] All dependencies are in `requirements.txt`
- [x] `app.py` is the main Streamlit application
- [x] Data files are accessible (or use cloud storage)
- [x] Environment variables are configured (if needed)
- [x] `.gitignore` excludes sensitive files

## 🔧 Configuration Files

All necessary deployment files have been created:

- ✅ `app.py` - Streamlit dashboard application
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Heroku configuration
- ✅ `setup.sh` - Heroku setup script
- ✅ `Dockerfile` - Docker container configuration
- ✅ `.streamlit/config.toml` - Streamlit configuration

## 🔐 Security Considerations

1. **Environment Variables**: Store API keys and secrets as environment variables
2. **Authentication**: Enable Streamlit Cloud authentication or add custom auth
3. **Data Access**: Consider using cloud storage (S3, GCS) for data files
4. **Rate Limiting**: Implement rate limiting for public dashboards

## 📊 Monitoring & Updates

- **Automatic Updates**: Most platforms auto-deploy on git push
- **Logs**: Check platform logs for errors
- **Monitoring**: Set up alerts for downtime
- **Backups**: Regular data backups recommended

## 🆘 Troubleshooting

### Common Issues:

1. **Port Configuration**: Ensure port is set correctly (`$PORT` or `8080`)
2. **Dependencies**: Check `requirements.txt` includes all packages
3. **Data Paths**: Use relative paths or environment variables
4. **Memory Limits**: Some free tiers have memory limits

### Getting Help:

- Streamlit Community: [discuss.streamlit.io](https://discuss.streamlit.io)
- Platform Documentation: Check respective platform docs
- GitHub Issues: Open an issue in the repository

## 🎯 Recommended Deployment Path

**For Beginners**: Streamlit Cloud (Option 1) - Easiest and free
**For Production**: Google Cloud Run or AWS Elastic Beanstalk
**For Quick Testing**: Railway or Heroku

---

**Need help?** Check the platform-specific documentation or open an issue in the repository.

