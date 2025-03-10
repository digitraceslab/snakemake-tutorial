import pandas as pd

input_fns = snakemake.input
output_fn = snakemake.output[0]

df = pd.read_csv(input_fns[0])

resampled_df = (
    df.assign(start_time=pd.to_datetime(df['start_time']))
      .set_index('start_time')
      .groupby('user_id')
      .resample('h')['duration']
      .sum()
      .reset_index()
)
resampled_df.to_csv(output_fn, index = False)
