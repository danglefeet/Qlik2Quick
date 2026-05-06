# Qlik2Quick

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-green)

---

**Migrate Qlik Sense QVF dashboards automatically into Amazon QuickSight datasets and analyses. Simplify your BI modernization journey.**

---

## 🚀 Quickstart Instructions

1. **Clone or download this repository.**

2. **Create and activate a virtual environment:**
   - Windows CMD: `setup.bat`
   - Windows PowerShell: `setup.ps1`
   - Linux/macOS: `setup.sh`

3. **Configure your AWS credentials in `config.json`:**
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

4. **Place your `.qvf` file(s)** into the project folder or a subfolder.

5. **Run the migration:**
```bash
python main.py your-dashboard.qvf
```
or for batch mode:
```bash
python main.py qvf_folder/
```

---

## ⚙️ Configuration Parameters

| Parameter | Description | Example |
|:---|:---|:---|
| `aws_access_key` | AWS IAM Access Key with QuickSight permissions | `AKIAxxxxxxxx` |
| `aws_secret_key` | AWS IAM Secret Key | `xxxxxxxxxxxxxxx` |
| `aws_region` | AWS Region (must match QuickSight region) | `us-east-1` |
| `quicksight_namespace` | Namespace under which assets will be deployed (e.g., `default`, `POC`) | `POC` |
| `default_database` | Default database if source uses Athena or Redshift | `default` |
| `default_s3_bucket` | Default S3 bucket if Athena is used | `my-athena-query-results` |

---

## 🔄 Basic Workflow

| Step | Description |
|:---|:---|
| 1 | Parse the `.qvf` file using `QVFParser`. |
| 2 | Translate Qlik charts and expressions using `QlikToQuickSightMapper`. |
| 3 | Upload datasets and visuals to Amazon QuickSight using `QuickSightUploader`. |
| 4 | Create and publish analyses dynamically under the configured namespace. |

---

## 📈 Supported Visual Types

- Bar Charts
- Line Charts
- Pie Charts
- KPI Cards
- Tables

Other unsupported or extension charts will gracefully default to a placeholder and log a warning.

---

## 📚 Batch Mode

You can process multiple `.qvf` files at once:

1. Place all `.qvf` files into a folder (e.g., `qvf_folder/`).
2. Run:
```bash
python main.py qvf_folder/
```
Each dashboard will be automatically parsed, mapped, and migrated sequentially.

---

## 🧠 Known Limitations

- Advanced Qlik objects (e.g., mashups, extensions) are not currently migrated.
- Complex Set Analysis expressions might require manual adjustment.
- Visual layout positioning (relative sizing) is not mapped yet.
- All field types are initially treated as `STRING`.

Future enhancements are detailed in the [ROADMAP.md](./ROADMAP.md).

---

## 🛣 Planned Enhancements

See [ROADMAP.md](./ROADMAP.md) for a full list of future features including:
- Smarter type inference
- Advanced visual formatting
- SaaS automation options
- Robust error recovery
- Expanded chart support

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE.md).

---

## 📷 Social Preview

![Qlik2Quick Logo](./assets/logo.png)

---

## 🏷️ Topics

`Qlik`, `Sense`, `AWS`, `Amazon`, `Quicksight`, `BI`, `Business Intelligence`, `Analytics`, `Data`, `Migrate`, `Migration`, `POC`

---

# 🎯 Final Tip

> Use Qlik2Quick to dramatically accelerate your BI cloud migration efforts and modernize legacy reporting ecosystems. 