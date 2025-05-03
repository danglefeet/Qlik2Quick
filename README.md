# Qlik2Quick: Qlik Sense to Amazon QuickSight Migration Proof of Concept

---

## 🚀 Quickstart Instructions

1. **Clone this repository** (or place your project files into a folder).

2. **Create the virtual environment and install dependencies:**
   - Run `setup.bat`, `setup.ps1`, or `setup.sh` depending on your platform.

3. **Prepare `config.json`** with the following structure:
```json
{
    "aws_access_key": "YOUR_AWS_ACCESS_KEY_HERE",
    "aws_secret_key": "YOUR_AWS_SECRET_KEY_HERE",
    "aws_region": "us-east-1",
    "quicksight_namespace": "POC",
    "default_database": "default",
    "default_s3_bucket": "your-default-s3-bucket-name"
}
```

4. **Place your Qlik Sense `.qvf` file(s)** in the working directory or a subfolder.

5. **Run the migration:**
```bash
python main.py your-dashboard.qvf
```
or for batch mode:
```bash
python main.py your-qvf-folder/
```

---

## ⚙️ Configuration Parameters Explained (`config.json`)
(unchanged)

---

## 🔄 Basic Workflow Process
(unchanged)

---

## 📈 Supported Visual Types
(unchanged)

---

## 🧠 Useful Information and Future Enhancements
(unchanged)

---

# 📋 Setup Options Based on Platform
(unchanged)

---

# 🛠 Example Main Workflow (`main.py`)

(unchanged)

---

# 📦 Batch Mode

**You can migrate multiple dashboards automatically by specifying a folder containing `.qvf` files.**

Example folder structure:
```
qvf_folder/
├── SalesDashboard.qvf
├── HRDashboard.qvf
├── FinanceDashboard.qvf
```

Command to run all at once:
```bash
python main.py qvf_folder/
```

Each QVF will be processed in sequence and migrated into QuickSight.

---

# ✅ Project Status
(unchanged)

---

# 🏁 Summary
(unchanged)