from googleapiclient.discovery import build
import os

class VideoLinkHelper:
    
    __api_key = 'AIzaSyDx-RnIaiMj6kSO-u0VEiPAKTRp74hJM84'

    def __init__(self):
        self.youtube = build('youtube', 'v3', developerKey=self.__api_key)

    def get_playlist_videos(self, playlist_id):

        # Request playlist items
        request = self.youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50  # Adjust for larger playlists (maximum 50 per request)
        )
        response = request.execute()

        # Extract video links
        video_links = []
        for item in response.get('items', []):
            video_id = item['snippet']['resourceId']['videoId']
            video_links.append(f"https://www.youtube.com/watch?v={video_id}")

        # Check for next page token for large playlists
        next_page_token = response.get('nextPageToken')
        while next_page_token:
            # Get videos from next page
            request = self.youtube.playlistItems().list(
                part='snippet',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()

            # Extract video links and update token
            for item in response.get('items', []):
                video_id = item['snippet']['resourceId']['videoId']
                video_links.append(f"https://www.youtube.com/watch?v={video_id}")
                next_page_token = response.get('nextPageToken')

        return video_links

    def create_VideoLink_txt(self, playlist_id):
        video_links = self.get_playlist_videos(playlist_id)
        if os.path.exists('videolinks.txt'):
            os.remove('videolinks.txt')
        f = open("videolinks.txt", "a")
        for i in video_links:
            f.write(i+'\n')

playlist_id = "PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV"
video = VideoLinkHelper()
video.create_VideoLink_txt(playlist_id)