print("\n\n\n\n" + "-" * 100 + "\n\n\n\n\n") # Console spacing

import bpy, sys, subprocess, os, time, threading, random, inspect # Safe built-in imports
print(f'line {inspect.currentframe().f_lineno}')
from datetime import datetime # Safe built-in import
print(f'line {inspect.currentframe().f_lineno}')

def bugprint(message, param3=None, param2=0, d={'w': '\033[97m', 'r': '\033[31m', 'red': '\033[31m', 'g': '\033[32m'}): print('\n' * (param2 if param3 in d else (param2 if isinstance(param3, int) else 0)) + d.get(param3, d.get(param2, '\033[97m')) + datetime.datetime.now().strftime('%I:%M:%S.%f')[:12] + ' ' + datetime.datetime.now().strftime('%p') + ': ' + message + '\033[0m' + '\n' * (param2 if param3 in d else (param2 if isinstance(param3, int) else 0)))

# Constants
HEARTBEAT_INTERVAL = 10 # Seconds between heartbeat updates
print(f'line {inspect.currentframe().f_lineno}')
RETRY_INTERVAL = 5 # Seconds between retry attempts
print(f'line {inspect.currentframe().f_lineno}')
PC_ID = f"pc{random.randint(10000, 99999)}" # e.g., "pc58392"
print(f'line {inspect.currentframe().f_lineno}')
DIR_PRIORITIES = [os.path.join(os.environ['USERPROFILE'], d) for d in ["Downloads", "Desktop", "Documents"]] # e.g., ["C:\\Users\\ns1995\\Downloads", "C:\\Users\\ns1995\\Desktop", "C:\\Users\\ns1995\\Documents"]
print(f'line {inspect.currentframe().f_lineno}')
MAIN_CLOUD_FOLDER     = "1YGVuw05zb1AQYwT_nkTOaRPi7kfkaKcJ" # Main Google Drive folder ID (fill this in)
print(f'line {inspect.currentframe().f_lineno}')
BlenderRenders_FOLDER = "12IbxfyVQd4Qn4_kF4hsVQAzm09R5rjad" # Blender renders folder ID
print(f'line {inspect.currentframe().f_lineno}')
SERVICE_ACCOUNT_JSON = r"""{
  "type": "service_account",
  "project_id": "blenderupload",
  "private_key_id": "8a1e8e9291ed5a354a633b104048c2eab95f0d14",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCifoiF4XlCrZMY\nnJPj7d8TO1mCdM02aH9w7ktt2fViFTxFckbQHMPvt2HJHPMdp20akBhsjAgiizkB\nj+7VOGchrHU/LSzUe7HOHuA1U/AGctEO3LH2IlPLPRNlD4rD7CeMhwKhmV+H6SHw\n8eREVLw/AeZnpfC2S624EWcA3SiEEZEc0O5C6nIgVnL2Friul3iRSFWvzvR+w62p\nwjY98jp8RN4nloxgW+Dn76UU7X1kCW8N4avN2/Py1SGTzCyJ9VIKXuVLNKuwwOZ1\nqW3BWU0YwGkBB03HTA+mbOcTtYzAQcQZ5uW/dgNwwl8kII4tJSzAasSOAzVR6nJx\nLCzhnHY5AgMBAAECggEAAksg6CrXiE5k3hsPp07rMB1NVR8K6nKtIc3rOKCz6u97\ny0sinrtZNJ/0/F6xO8DqNE7GWXncf4hRhKkgaNgD9KC3gu3DTTh1uQAMkBQgNicW\ntkv9Iwk2/45cILgIcF177WrWaat9grCSrxDq9N/xTD5dnybjb98/k3KDbqqwcLS8\n+IwKpY86vFNrxBbOdo3Uk2uJvxTiOCRAQlq3epHfFKZqJTDQ0kGLDkC9fJ8FY/We\njmmaFjHGoGbSOinmqDm751hJiK3qBUl7rM1uWbpU8ud6xqGjm+HMfo/mWTOZW0y2\nNBCXIa8vnVpY191ABuKg8HMDuuRCNStLO74Dy+IfUQKBgQDlUq0clKJAgZvyxK36\nM2ay4hFsBouXMzSw9S750iDzIy1pMkHICms8+IdkNRlU+vRkmis14utr2ZnT90PV\nR6oq1xrvG5WklxhD2uRjP/FCAuHVMxBR5EQvwbALENaPwulk9qP/oY3EF4ddCqBN\ngfbk/EvsHPGzXNQOfCsLhuKy1QKBgQC1Zax7uEePApgoUehz7xIEKYJr15V6WP1N\nWc47PB5QVi/ePDEP3tVuk9t0zfnLJhq1wXAGt8cRUh6fiR/GwcUqxrlXD2S3D9U0\nGX6z1i6RP0OunoZHBTxarHJvxXIRf2bmiJyDg/FMNPxoKhSf1eWKuDuUG9SX+sKy\n0p4t1i5/1QKBgQCNikPyugKTEewxIRfIr+UZT9M0+604u5AwEITYCMvxharHnQ9g\n6p1Z2oOmY+eoveQOG+HDtrVbscjyPVGO2Fa9blrfbgUku2VsrDP+1j6QYbsFnija\ngqtbVo7TpabowILRoDGE3C/l8ifIU4Cxlh/PIbGyoALGk+sGrbjbuns9qQKBgH06\noAUZh21XYSwUv+Gpnkp5TaydvHgmj1ijMxj5vAPCPHG0JDrMn5QjR1IwEM8Kk03/\nKRO6NBflFXcV93YDt9Z8Mt/DpMgsigfZwfrtVmC3yEX48sJ8/tmqS6aWLNWfmq50\niXjR0ffGbKqMwohF5p4J6jepru7tExTZCpKiVp+xAoGBAKbPwPaQ5x9lKTC6EMNs\nr31pHJWPUmnZvHuYA25+dKNr+FfLZrPV9PZTlkHVUfEoaZHoM30sy+TYEcEinJWw\nxV7Z31scICCQDgPIzGL53Ovd4ENdUw4qIbpBfxqxYzqtX85Auny7/VHGrE7KQ0Sk\nCqbEWV4SkgjxflpMZzGzAWW8\n-----END PRIVATE KEY-----\n",
  "client_email": "blender-uploader@blenderupload.iam.gserviceaccount.com",
  "client_id": "106711238218850717302",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/blender-uploader%40blenderupload.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}"""
print(f'line {inspect.currentframe().f_lineno}')

# Check and install packages if needed
for pkg in ["google-api-python-client", "google-auth-httplib2", "google-auth-oauthlib"]:
    if subprocess.call([sys.executable, "-m", "pip", "show", pkg], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
        bugprint(f"{pkg} found") # e.g., "03:45:23.456 PM: google-api-python-client found" in white
        print(f'line {inspect.currentframe().f_lineno}')
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg]) # Install only if not found
        print(f'line {inspect.currentframe().f_lineno}')
try:
    subprocess.check_call([sys.executable, "-m", "ensurepip"])
    print(f'line {inspect.currentframe().f_lineno}')
except subprocess.CalledProcessError as e:
    bugprint(f"Error installing pip: {e}", 'r', newlines=1) # e.g., "\n03:45:23.456 PM: Error installing pip: [Errno 2] No such file or directory\n" in red
    print(f'line {inspect.currentframe().f_lineno}')

bugprint("Starting renderfarm") # e.g., "03:45:23.456 PM: Starting renderfarm" in white
print(f'line {inspect.currentframe().f_lineno}')

# Now safe to import Google API dependencies
import json
print(f'line {inspect.currentframe().f_lineno}')
import ssl
print(f'line {inspect.currentframe().f_lineno}')
import httplib2
print(f'line {inspect.currentframe().f_lineno}')
from google.oauth2 import service_account
print(f'line {inspect.currentframe().f_lineno}')
from googleapiclient.discovery import build
print(f'line {inspect.currentframe().f_lineno}')
from googleapiclient.http import MediaFileUpload
print(f'line {inspect.currentframe().f_lineno}')
bugprint("Imported google api") # e.g., "03:45:23.456 PM: Imported google api" in white
print(f'line {inspect.currentframe().f_lineno}')


# Find blend file across priority dirs and script relatives
def find_blend_file():
    for dir in DIR_PRIORITIES: # Check priority directories first
        for f in os.listdir(dir):
            if f.endswith('.blend'): return dir, f
            print(f'line {inspect.currentframe().f_lineno}')
        print(f'line {inspect.currentframe().f_lineno}')
    script_dir = os.path.dirname(os.path.abspath(__file__)) # e.g., "C:\\Users\\ns1995\\Downloads\\script_folder"
    print(f'line {inspect.currentframe().f_lineno}')
    for level in [script_dir, os.path.dirname(script_dir), os.path.dirname(os.path.dirname(script_dir))]: # Parent, grandparent, great-grandparent
        for f in os.listdir(level):
            if f.endswith('.blend'): return level, f
            print(f'line {inspect.currentframe().f_lineno}')
        print(f'line {inspect.currentframe().f_lineno}')
    raise FileNotFoundError("No .blend file found")
    print(f'line {inspect.currentframe().f_lineno}')

MAIN_LOCAL_FOLDER, blend_file = find_blend_file() # e.g., "C:\\Users\\ns1995\\Downloads", "animation_view.blend"
print(f'line {inspect.currentframe().f_lineno}')
BLEND_FILE = os.path.join(MAIN_LOCAL_FOLDER, blend_file) # e.g., "C:\\Users\\ns1995\\Downloads\\animation_view.blend"
print(f'line {inspect.currentframe().f_lineno}')
blend_name = os.path.splitext(blend_file)[0].replace('_view', '') # e.g., "animation"
print(f'line {inspect.currentframe().f_lineno}')
OUTPUT_DIR = os.path.join(MAIN_LOCAL_FOLDER, f"output_{blend_name}") # e.g., "C:\\Users\\ns1995\\Downloads\\output_animation"
print(f'line {inspect.currentframe().f_lineno}')

# Authenticate with Google Drive
def get_drive_service():
    creds = service_account.Credentials.from_service_account_info(json.loads(SERVICE_ACCOUNT_JSON), scopes=["https://www.googleapis.com/auth/drive"])
    print(f'line {inspect.currentframe().f_lineno}')
    http = httplib2.Http(); http.ssl_version = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2) # Force TLS 1.2
    print(f'line {inspect.currentframe().f_lineno}')
    return build("drive", "v3", credentials=creds, http=http)
    print(f'line {inspect.currentframe().f_lineno}')

# Upload file to Google Drive with retry
def upload_to_drive(service, file_path, folder_id, max_retries=5):
    for attempt in range(max_retries):
        try:
            if not os.path.exists(file_path):
                bugprint(f"Error: File not found: {file_path}", 'r', newlines=1) # e.g., "\n03:45:23.456 PM: Error: File not found: C:\\Users\\ns1995\\Downloads\\output_animation\\animation_0001.tif\n" in red
                print(f'line {inspect.currentframe().f_lineno}')
                return
                print(f'line {inspect.currentframe().f_lineno}')
            media = MediaFileUpload(file_path)
            print(f'line {inspect.currentframe().f_lineno}')
            service.files().create(body={"name": os.path.basename(file_path), "parents": [folder_id]}, media_body=media, fields="id").execute()
            print(f'line {inspect.currentframe().f_lineno}')
            return
            print(f'line {inspect.currentframe().f_lineno}')
        except Exception as e:
            if attempt == max_retries - 1: raise e # Raise on last attempt
            print(f'line {inspect.currentframe().f_lineno}')
            time.sleep(RETRY_INTERVAL) # Use retry interval
            print(f'line {inspect.currentframe().f_lineno}')

# Create, upload, and destroy text file
def create_upload_txt(service, title, text, folder_id):
    file_path = f"{title}.txt" # e.g., "animation_pc58392_notification.txt"
    print(f'line {inspect.currentframe().f_lineno}')
    with open(file_path, "w") as f: f.write(text)
    print(f'line {inspect.currentframe().f_lineno}')
    upload_to_drive(service, file_path, folder_id)
    print(f'line {inspect.currentframe().f_lineno}')
    os.remove(file_path)
    print(f'line {inspect.currentframe().f_lineno}')

# Render frame
def render_frame(frame_num, output_path, scene):
    bpy.context.scene.frame_set(frame_num)
    print(f'line {inspect.currentframe().f_lineno}')
    bpy.context.scene.render.filepath = output_path
    print(f'line {inspect.currentframe().f_lineno}')
    start_time = time.time()
    print(f'line {inspect.currentframe().f_lineno}')
    bpy.ops.render.render(write_still=True)
    print(f'line {inspect.currentframe().f_lineno}')
    return time.time() - start_time # Return render duration
    print(f'line {inspect.currentframe().f_lineno}')

# Heartbeat thread
def heartbeat_thread(drive_service, sample_count=1024):
    while True:
        try:
            status_file = f"{blend_name}_{PC_ID}_status" # e.g., "animation_pc58392_status"
            print(f'line {inspect.currentframe().f_lineno}')
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # e.g., "2025-03-08 14:30:45.123"
            print(f'line {inspect.currentframe().f_lineno}')
            text = f"Progress - Samples: {sample_count}\nTime: {current_time}"
            print(f'line {inspect.currentframe().f_lineno}')
            create_upload_txt(drive_service, status_file, text, MAIN_CLOUD_FOLDER)
            print(f'line {inspect.currentframe().f_lineno}')
            bugprint(f"Heartbeat: Samples {sample_count} at {current_time}") # e.g., "03:45:23.456 PM: Heartbeat: Samples 1024 at 2025-03-08 14:30:45.123" in white
            print(f'line {inspect.currentframe().f_lineno}')
        except Exception as e:
            bugprint(f"Heartbeat error: {e}", 'r', newlines=1) # e.g., "\n03:45:23.456 PM: Heartbeat error: [Errno 13] Permission denied\n" in red
            print(f'line {inspect.currentframe().f_lineno}')
        time.sleep(HEARTBEAT_INTERVAL) # Use heartbeat interval
        print(f'line {inspect.currentframe().f_lineno}')

# Main execution with retry loop
while True:
    try:
        if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR) # Create output dir
        print(f'line {inspect.currentframe().f_lineno}')
        
        # Load scene
        bpy.ops.wm.open_mainfile(filepath=BLEND_FILE)
        print(f'line {inspect.currentframe().f_lineno}')
        scene = bpy.context.scene
        print(f'line {inspect.currentframe().f_lineno}')
        
        # Fix fluid and smoke caches
        for obj_name, cache_path in [("fluid_surface.003", "simulations/simulations/coffee_fluid.abc"), 
                                   ("Coffee machine vapor", "simulations/simulations/coffee_machine_vapor"), 
                                   ("Lone cup vapor", "simulations/simulations/final_view_coffee_vapor")]:
            if obj_name in bpy.data.objects:
                obj = bpy.data.objects[obj_name]
                print(f'line {inspect.currentframe().f_lineno}')
                try:
                    if "MeshSequenceCache" in obj.modifiers or "Fluid" in obj.modifiers or "Smoke" in obj.modifiers:
                        if not os.path.exists(obj.modifiers[0].filepath): # Check if cache is missing
                            full_path = os.path.join(MAIN_LOCAL_FOLDER, cache_path) # e.g., "C:\\Users\\ns1995\\Downloads\\simulations\\simulations\\coffee_fluid.abc"
                            print(f'line {inspect.currentframe().f_lineno}')
                            if not os.path.exists(full_path): # Search if not found
                                for dir in DIR_PRIORITIES + [os.path.dirname(os.path.dirname(__file__))]:
                                    if os.path.exists(os.path.join(dir, cache_path)): full_path = os.path.join(dir, cache_path); break
                                    print(f'line {inspect.currentframe().f_lineno}')
                                print(f'line {inspect.currentframe().f_lineno}')
                            obj.modifiers[0].filepath = full_path
                            print(f'line {inspect.currentframe().f_lineno}')
                            bugprint(f"Fixed cache for {obj_name} to {full_path}") # e.g., "03:45:23.456 PM: Fixed cache for fluid_surface.003 to C:\\Users\\ns1995\\Downloads\\simulations\\simulations\\coffee_fluid.abc" in white
                            print(f'line {inspect.currentframe().f_lineno}')
                except:
                    bugprint(f"Could not fix cache for {obj_name}", 'r', newlines=1) # e.g., "\n03:45:23.456 PM: Could not fix cache for fluid_surface.003\n" in red
                    print(f'line {inspect.currentframe().f_lineno}')
            print(f'line {inspect.currentframe().f_lineno}')

        # Enable compute device type
        try:
            bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'OPTIX'
            print(f'line {inspect.currentframe().f_lineno}')
            bpy.context.preferences.addons['cycles'].preferences.get_devices()
            print(f'line {inspect.currentframe().f_lineno}')
            for device in bpy.context.preferences.addons['cycles'].preferences.devices: device.use = True
            print(f'line {inspect.currentframe().f_lineno}')
        except Exception as e:
            bugprint(f"compute device type setup failed: {e}", 'r', newlines=1) # e.g., "\n03:45:23.456 PM: compute device type setup failed: compute device type not available\n" in red
            print(f'line {inspect.currentframe().f_lineno}')

        # Render settings
        scene.render.resolution_x = 2560 # 1440p 16:9
        print(f'line {inspect.currentframe().f_lineno}')
        scene.render.resolution_y = 1440
        print(f'line {inspect.currentframe().f_lineno}')
        samples = 1024 # Default sample count for heartbeat tracking
        print(f'line {inspect.currentframe().f_lineno}')
        # scene.cycles.samples = 512 # Uncomment to set samples
        # scene.cycles.adaptive_threshold = 0.01 # Uncomment to set noise threshold
        scene.render.image_settings.file_format = 'TIFF'
        print(f'line {inspect.currentframe().f_lineno}')

        drive_service = get_drive_service()
        print(f'line {inspect.currentframe().f_lineno}')
        threading.Thread(target=heartbeat_thread, args=(drive_service, samples), daemon=True).start() # Start heartbeat
        print(f'line {inspect.currentframe().f_lineno}')

        # Render and upload frames
        for frame in range(scene.frame_start, scene.frame_end + 1):
            frame_str = f"{frame:04d}" # e.g., "0001"
            print(f'line {inspect.currentframe().f_lineno}')
            output_path = os.path.join(OUTPUT_DIR, f"{blend_name}_{frame_str}") # e.g., "C:\\Users\\ns1995\\Downloads\\output_animation\\animation_0001"
            print(f'line {inspect.currentframe().f_lineno}')
            render_time = render_frame(frame, output_path, scene)
            print(f'line {inspect.currentframe().f_lineno}')
            rendered_file = f"{output_path}.tif" # e.g., "C:\\Users\\ns1995\\Downloads\\output_animation\\animation_0001.tif"
            print(f'line {inspect.currentframe().f_lineno}')
            bugprint(f"Saved {rendered_file} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}") # e.g., "03:45:23.456 PM: Saved C:\\Users\\ns1995\\Downloads\\output_animation\\animation_0001.tif at 2025-03-08 14:30:45.123" in white
            print(f'line {inspect.currentframe().f_lineno}')
            
            # Adjust settings if render takes too long
            if render_time > 600: # 10 minutes
                scene.render.resolution_x, scene.render.resolution_y = 1920, 1080
                print(f'line {inspect.currentframe().f_lineno}')
                if render_time > 850:
                    scene.cycles.adaptive_threshold = 0.01
                    print(f'line {inspect.currentframe().f_lineno}')
                if render_time > 1200:
                    samples = scene.cycles.samples = int(samples * 0.75) 
                    print(f'line {inspect.currentframe().f_lineno}')
                elif render_time > 1800: # Still too long
                    samples = scene.cycles.samples = int(samples * 0.5)
                    print(f'line {inspect.currentframe().f_lineno}')
                    notify = f"Reduced samples to {samples} for frame {frame}" # e.g., "Reduced samples to 256 for frame 1"
                    print(f'line {inspect.currentframe().f_lineno}')
                    create_upload_txt(drive_service, f"{blend_name}_{PC_ID}_notification", notify, MAIN_CLOUD_FOLDER)
                    print(f'line {inspect.currentframe().f_lineno}')
                    bugprint(notify) # e.g., "03:45:23.456 PM: Reduced samples to 256 for frame 1" in white
                    print(f'line {inspect.currentframe().f_lineno}')
                bpy.ops.wm.save_mainfile(filepath=BLEND_FILE) # Save blend file after adjustments
                print(f'line {inspect.currentframe().f_lineno}')

            upload_to_drive(drive_service, rendered_file, BlenderRenders_FOLDER)
            print(f'line {inspect.currentframe().f_lineno}')
            print("\n\n\n\n" + "-" * 100 + "\n\n\n\n\n") # Console spacing after upload
            print(f'line {inspect.currentframe().f_lineno}')

        break # Exit retry loop on success
        print(f'line {inspect.currentframe().f_lineno}')

    except Exception as e:
        error_msg = f'line {inspect.currentframe().f_lineno}: {str(e)}' # e.g., "\n03:45:23.456 PM: line 150: [Errno 2] No such file or directory\n" in red
        print(f'line {inspect.currentframe().f_lineno}')
        bugprint(error_msg, 'r', newlines=1)
        print(f'line {inspect.currentframe().f_lineno}')
        create_upload_txt(get_drive_service(), f"{blend_name}_{PC_ID}_error", error_msg, MAIN_CLOUD_FOLDER) # e.g., "animation_pc58392_error.txt"
        print(f'line {inspect.currentframe().f_lineno}')
        time.sleep(RETRY_INTERVAL) # Use retry interval
        print(f'line {inspect.currentframe().f_lineno}')