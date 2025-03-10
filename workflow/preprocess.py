import pandas as pd 

# Load data
def load(input_fns) -> pd.DataFrame:
    raise NotImplementedErrror

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
    raise NotImplementedError

if __name__ == '__main__':

    # TODO: get input/output paths from snakemake
    #input_fns = 
    #output_fn = 

    data = load(input_fns=input_fns)
    
    processed_data = process(data)
    save(data, output_fn=output_fn)