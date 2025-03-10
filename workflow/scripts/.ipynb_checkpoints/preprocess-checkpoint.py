import pandas as pd 

# Load data
def load(input_fns) -> pd.DataFrame:

    res = []
    for i, input_fn in enumerate(input_fns):
        df = pd.read_csv(input_fn)
        df['user_id'] = f'u{i}'
        res.append(df)
        
    return pd.concat(res)

# Process stuffs
# Turn the data into call duration and resample to hourly level
def process(df):

    # Clean columns' names by removing trailling space
    df.columns = df.columns.str.strip()

    # Compute call duration
    df["duration"] = df["end_timestamp"] - df["start_timestamp"]

    # Convert start time to datetime
    df["start_time"] = pd.to_datetime(df["start_timestamp"], unit="s")

    df['mock'] = 'dummy'
    return df

# Save data 
def save(df, output_fn):
    df.to_csv(output_fn, index = False)

if __name__ == '__main__':

    input_fns = snakemake.input
    output_fn = snakemake.output[0]

    data = load(input_fns=input_fns)
    
    processed_data = process(data)
    save(data, output_fn=output_fn)
