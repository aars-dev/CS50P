def get_media_type(filename):
    # Convert the filename to lowercase for case-insensitive comparison
    filename = filename.lower().strip()

    # Define dictionary mapping file extensions to media types
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Check if the filename ends with any of the specified suffixes
    for suffix in media_types:
        if filename.endswith(suffix):
            return media_types[suffix]

    # If the filename doesn't match any suffix, return default media type
    return 'application/octet-stream'

def main():
    filename = input("File name: ")
    media_type = get_media_type(filename)
    print(media_type)

main()
