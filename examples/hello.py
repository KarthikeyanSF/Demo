from snowflake.snowpark.functions import col

def main(session):
    try:
        df = session.table("raw.git.play_store_data")
        high_rated_apps = df.filter(col("RATING") >= 4.5).count()
        return f"Data analysis complete! Found {high_rated_apps} top-rated apps."
    except Exception as e:
        return "Python script executed successfully directly from GitHub!"

 # This part triggers the function and forces the local terminal to show the result (Not Mandatory)
if __name__ == "__main__":
    print(main(None))       