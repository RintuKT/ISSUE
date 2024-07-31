from googleapiclient.discovery import build

api_key = 'AIzaSyDOHaidZTkmFhqZW9GCEjfoY1XXRJni5aQ'

youtube = build('youtube', 'v3', developerKey = api_key)