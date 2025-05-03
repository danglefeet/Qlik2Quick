# 📍 Qlik2Quick Roadmap

---

## ✅ Initial Release (v1.0.0)
- Parse `.qvf` files
- Translate basic Qlik expressions to QuickSight syntax
- Migrate Sheets, Charts, KPIs, and Tables
- Batch processing of multiple QVFs
- Basic dataset creation and SPICE import
- Platform-specific setup scripts (Windows CMD, PowerShell, Linux/macOS Bash)

---

## 🛣 Planned Enhancements

### 🧠 Smarter Data Type Mapping
- Infer numeric, date, and boolean field types from Qlik metadata
- Auto-apply correct QuickSight data types

### 🛠️ Full Visual Customization
- Support axis titles, legends, and tooltips
- Handle stacked vs grouped bar charts
- KPI formatting (prefixes, suffixes, thresholds)

### 📊 Multi-Source Support
- Direct Athena and Redshift source linking
- Expand support for S3-based datasets

### 🔒 Security Enhancements
- Environment variable support for AWS credentials
- Optional IAM Role usage instead of static credentials

### 🌐 Internationalization
- Support for non-English Qlik Sense apps

### 🖼️ Layout Mapping
- Attempt spatial positioning of objects on QuickSight sheets based on Qlik sheets

### 🛡️ Error Handling and Recovery
- Better handling of partial migration failures
- Detailed migration logs

---

## 🚀 Stretch Goals

### 🎨 Custom Dashboard Template System
- Ability to choose different QuickSight themes at migration time
- Pre-built template layouts

### 🛡️ Validation and Testing
- Validate expression accuracy post-migration
- Compare record counts between Qlik and QuickSight datasets

### 🤖 SaaS Automation
- Expose Qlik2Quick as an internal microservice with REST API
- Drag-and-drop QVF web UI for migration

---

# 📢 Community Contributions Welcome
If you'd like to contribute:
- Fork the repository
- Create a feature branch
- Submit a pull request 🚀