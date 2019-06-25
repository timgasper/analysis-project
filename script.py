import datadotworld as dw
ds = dw.load_dataset('democorp/salesforce-data', auto_update=True)
salesforce_data = ds.dataframes['sales_pipeline']

