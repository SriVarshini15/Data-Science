# Install required package (Uncomment if running for the first time)
# !pip install google-api-python-client pandas seaborn openpyxl

# Import required modules
from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

# Set up the YouTube API
api_key = 'AIzaSyAj-msXnzaLH8z_Gx6E05gCVoZ1JqNpCrc'  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=api_key)

# List of YouTube channel IDs
channel_ids = [
    'UCnz-ZXXER4jOvuED5trXfEA',  # Example Channel
    'UCZSNzBgFub_WWil6TOTYwAg',  # Netflix India
    'UC8md0UEGj7UbjcZtMjBVrgQ',  # Behindwoods TV
    'UC4zWG9LccdWGUlF77LZ8toA',  # Prime Video India
    'UC8lPjTzRiG37n1Q2kpz3Rfg',  # JioHotstar Tamil
    'UCq-Fj5jknLsUf-MWSy4_brA',  # TED
    'UCX6OQ3DkcsbYNE6H8uQQuVA',  # MrBeast
    'UCVTlvUkGslCV_h-nSAId8Sw',  # Amazon Prime Video
    'UC-lHJZR3Gqxm24_Vd_AJ5Yw',  # PewDiePie
    'UCbfYPyITQ-7l4upoX8nvctg',  # Simplilearn
    'UClcE-kVhqyiHCcjYwcpfj9w',  # Sony SAB
    'UCYfdidRxbB8Qhf0Nx7ioOYw',  # SET India
    'UCsTcErHg8oDvUnTzoqsYeNw',  # The Viral Fever (TVF)
    'UCqwUrj10mAEsqezcItqvwEw',  # T-Series
    'UCj22tfcQrWG7EMEKS0qLeEg',  # Sony Music India
    'UC3XTzVzaHQEd30rQbuvCtTQ',  # National Geographic
    'UCY30JRSgfhYXA6i6xX1erWg',  # Dream
    'UCpEhnqL0y41EpW2TvWAHD7Q',  # BBC News
    'UC0v-tlzsn0QZwJnkiaUSJVQ',  # Netflix
    'UCXgGY0wkgOzynnHvSEVmE3A',  # Tech Burner
]
# Function to get YouTube channel statistics
def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    response = request.execute()

    data = dict(
        Channel_name=response['items'][0]['snippet']['title'],
        Subscribers=int(response['items'][0]['statistics']['subscriberCount']),
        Views=int(response['items'][0]['statistics']['viewCount']),
        Total_videos=int(response['items'][0]['statistics']['videoCount'])
    )

    return data

# Get stats for all channels
channel_data = [get_channel_stats(youtube, channel_id) for channel_id in channel_ids]

# Convert to Pandas DataFrame
df = pd.DataFrame(channel_data)

# Display the DataFrame
print(df)

# Set figure size for plots
sns.set(rc={'figure.figsize':(10, 6)})

# Plot bar charts
sns.barplot(x='Channel_name', y='Subscribers', data=df)
sns.barplot(x='Channel_name', y='Views', data=df)
sns.barplot(x='Channel_name', y='Total_videos', data=df)

# Save DataFrame to an Excel file
file_name = "youtube_channel_stats.xlsx"
df.to_excel(file_name, index=False)

# Uncomment below lines if running in Google Colab to download the file
# from google.colab import files
# files.download(file_name)
