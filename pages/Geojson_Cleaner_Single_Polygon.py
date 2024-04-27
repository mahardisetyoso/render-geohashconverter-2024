import streamlit as st
import json

def convert_geojson(geojson_data):
  """Converts GeoJSON data to a desired GeoJSON structure.

  Args:
      geojson_data (dict): The loaded GeoJSON data from the uploaded file.

  Returns:
      dict: The desired GeoJSON structure containing the geometry of the first feature.
  """
  desired_feature = {
      "type": "Feature",
      "properties": {},
      "geometry": geojson_data["features"][0]["geometry"]
  }
  return desired_feature

def main():
  """Streamlit app to upload and convert GeoJSON files."""

  # Upload GeoJSON file
  uploaded_file = st.file_uploader("Choose a GeoJSON file to convert")

  if uploaded_file is not None:
    # Load GeoJSON data (assuming valid JSON)
    geojson_data = json.loads(uploaded_file.read())  # Parse uploaded content

    # Convert GeoJSON data (assuming valid GeoJSON)
    converted_data = convert_geojson(geojson_data)

    # Download converted GeoJSON data (optional)
    save = st.text_input('Write you files name here and press ENTER!!')
    st.download_button(
        label="Download Clean GeoJSON",
        data=json.dumps(converted_data),
        file_name=save + '.geojson',
        mime="application/json",
    )

    # Access and display data from geojson_data (assuming valid GeoJSON)
    # ... your code to access geometry or other elements

if __name__ == "__main__":
  main()
