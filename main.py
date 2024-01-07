from script import download_video, download_playlist


def main():
    choice = input("\n//*// Select download roles//*//\n\n1- Enter 'v' for single video.\n2- Enter 'p' for playlist.\n\nPlease enter "
                   "your choice: ")
    url = input("Enter the YouTube URL: ")
    save_path = input("Enter the directory to save the video(s): ")

    if choice.lower() == 'v':
        download_video(url, save_path)
    elif choice.lower() == 'p':
        download_playlist(url, save_path)
    else:
        print("Invalid choice. Please enter 'v' or 'p'.")


if __name__ == "__main__":
    main()
