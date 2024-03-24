import asyncio
import os
from subprocess import PIPE

# Assuming LOGGER, leech_file, and format_filename are defined elsewhere

async def change_metadata_title(user_id, file_, custom_metadata):
    # Define the FFMPEG command to change metadata title
    ffmpeg_cmd = [
        "ffmpeg", "-i", file_, "-map", "0",
        "-metadata:s:s", f"title={custom_metadata}",
        "-metadata:s:v", f"title={custom_metadata}",
        "-metadata:s:a", f"title={custom_metadata}",
        "-c:v", "copy", "-c:a", "copy", "-c:s", "copy",
        "-y", f"{file_}.tmp"
    ]

    # Execute FFMPEG command asynchronously
    process = await asyncio.create_subprocess_exec(*ffmpeg_cmd, stderr=PIPE)
    _, stderr = await process.communicate()

    if process.returncode != 0:
        # FFMPEG command failed, handle the error
        error_message = stderr.decode().strip()
        LOGGER.error(f"FFMPEG metadata title change failed: {error_message}")
        return None
    else:
        # FFMPEG command succeeded, rename the file
        os.rename(f"{file_}.tmp", file_)
        return file_

async def upload(self, user_id, file_, dirpath, metadata, custom_metadata=None):  
    # Check if self is an instance of MyClass
    if not isinstance(self, MyClass):
        print("Error: 'self' is not an instance of MyClass.")
        return

    # Now, you can safely call __prepare_file method on self
    cap_mono, file_ = await self.__prepare_file(file_, dirpath)
    if cap_mono is None or file_ is None:
        print("Error: __prepare_file returned None.")
        return

    # If metadata is requested, edit the metadata before further processing
    if metadata:
        # Leech the file first
        leech_success = await leech_file(file_, dirpath)

        # If leeching is successful, proceed with metadata editing
        if leech_success:
            file_ = await change_metadata_title(user_id, file_, metadata)
        else:
            print("Error: File leeching failed.")
            return

    # Now, proceed with formatting the filename
    file_, cap_mono = await format_filename(file_, user_id, dirpath=dirpath, metadata=metadata)

# Sample usage
async def main():
    user_id = "user123"
    file_ = "input.mp4"
    dirpath = "/path/to/directory"
    metadata = True  # Set to True if metadata editing is required
    custom_metadata = "Custom Metadata"  # Optional custom metadata

    # Assuming self is an instance of some class with __prepare_file method
    my_instance = MyClass()
    await upload(my_instance, user_id, file_, dirpath, metadata, custom_metadata)

# Ensure to call main() in an asyncio environment
asyncio.run(main())
