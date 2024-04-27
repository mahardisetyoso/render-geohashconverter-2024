import json
import os
import shutil
import tempfile
import streamlit as st
from zipfile import ZipFile
import io

# Function to extract and save each polygon as a separate GeoJSON file,
# deleting the "name" attribute
column_data_att = st.text_input('Please put your column name of GeoJSON data here and please push ENTER!!!' )
def extract_polygons(geojson_data):
    temp_dir = tempfile.mkdtemp()  # Create temporary directory

    try:
        for feature in geojson_data["features"]:
            polygon_name = feature["properties"][column_data_att]
            file_path = os.path.join(temp_dir, f"{polygon_name}.geojson")

            # Delete the "name" attribute before saving
            del feature["properties"][column_data_att]

            with open(file_path, "w") as f:
                json.dump(feature, f)

    except Exception as e:
        st.error(f"Error occurred: {e}")

    return temp_dir

# Main Streamlit app (unchanged except for column name prompt)
def main():
    st.title("GeoJSON Country Extractor")

    uploaded_file = st.file_uploader("Upload GeoJSON", type=["geojson"])
    save = st.text_input('Write you files name here and press ENTER!!')
    if uploaded_file:
        geojson_data = json.load(uploaded_file)

        if st.button("Extract Countries"):
            temp_dir = extract_polygons(geojson_data)

            try:
                buffer = io.BytesIO()
                with ZipFile(buffer, "w") as zipf:
                    for root, _, files in os.walk(temp_dir):
                        for file in files:
                            file_path = os.path.join(root, file)
                            zipf.write(file_path, arcname=os.path.relpath(file_path, temp_dir))

                filename = save + '.zip'
                download_link = st.download_button(label="Download Countries", data=buffer.getvalue(),
                                                    file_name=filename, mime="application/zip")
                st.success(f"GeoJSON files extracted and saved as {filename}")
            except Exception as e:
                st.error(f"Error occurred during download: {e}")
            finally:
                shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
