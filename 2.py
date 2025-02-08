from youtube_transcript_api import YouTubeTranscriptApi

def transcribe_youtube_video(video_id):
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine the transcript into a single string
        transcript_text = ' '.join([entry['text'] for entry in transcript])

        return transcript_text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example YouTube video ID
    video_id = "v0YEaeIClKY"
    transcription = transcribe_youtube_video(video_id)
    print(transcription)
