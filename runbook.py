# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Install dbt dependencies
# Install dbt packages from requirements.txt
%pip install --upgrade -r /Workspace/Users/vyshnavprasad.va@gmail.com/demodbt/requirements.txt

# COMMAND ----------

# DBTITLE 1,Set up Databricks authentication
import os

os.environ['DB_TOKEN'] = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

print("✓ Authentication configured")

# COMMAND ----------

# DBTITLE 1,Navigate to dbt project directory
# MAGIC %cd /Workspace/Users/vyshnavprasad.va@gmail.com/demodbt/demodbt
# MAGIC !pwd
# MAGIC !ls -la

# COMMAND ----------

# DBTITLE 1,dbt Debug - Verify connection
# MAGIC %cd /Workspace/Users/vyshnavprasad.va@gmail.com/demodbt/demodbt
# MAGIC !dbt debug --profiles-dir .

# COMMAND ----------

# DBTITLE 1,dbt Deps - Install dependencies (if packages.yml exists)
# MAGIC %cd /Workspace/Users/vyshnavprasad.va@gmail.com/demodbt/demodbt
# MAGIC
# MAGIC import os
# MAGIC if os.path.isfile("packages.yml"):
# MAGIC     os.system("dbt deps --profiles-dir .")
# MAGIC else:
# MAGIC     print("No packages.yml found - skipping dbt deps")

# COMMAND ----------

# DBTITLE 1,dbt Run - Execute all models
!cd /Workspace/Users/vyshnavprasad.va@gmail.com/demodbt/demodbt
!dbt run --profiles-dir .

# Alternative: Run specific models
# dbt run --select l1_bronze --profiles-dir .
# dbt run --select l2_silver --profiles-dir .
# dbt run --select l3_golden --profiles-dir .

# COMMAND ----------

# DBTITLE 1,dbt Test - Run all tests
# MAGIC %undefined
# MAGIC cd /Workspace/Users/vyshnavprasad.va@gmail.com/demodbt/demodbt
# MAGIC dbt test --profiles-dir .

# COMMAND ----------

# DBTITLE 1,Other useful dbt commands
# MAGIC %md
# MAGIC ## Common dbt Commands
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ```bash
# MAGIC
# MAGIC     # Build everything (run + test)
# MAGIC     dbt build --profiles-dir .
# MAGIC
# MAGIC     # Run specific models
# MAGIC     dbt run --select model_name --profiles-dir .
# MAGIC
# MAGIC     # Run models in a specific schema
# MAGIC     dbt run --select l1_bronze --profiles-dir .
# MAGIC
# MAGIC     # Generate documentation
# MAGIC     dbt docs generate --profiles-dir .
# MAGIC
# MAGIC     # Run for production
# MAGIC     dbt run --target prod --profiles-dir .
# MAGIC
# MAGIC     # Seed data
# MAGIC     dbt seed --profiles-dir .
# MAGIC
# MAGIC     # Fresh check
# MAGIC     dbt source freshness --profiles-dir .
# MAGIC
# MAGIC     # Full refresh (for incremental models)
# MAGIC     dbt run --full-refresh --profiles-dir .
# MAGIC     
# MAGIC ```
# MAGIC ---

# COMMAND ----------


