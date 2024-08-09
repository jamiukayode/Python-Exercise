#pip install folium  || IPython       8/8/2024

import folium
from IPython.display import display

# Correcting the longitude for New York (should be negative)
map_center = [40.7128, -74.0060] # New York
mymap = folium.Map(location=map_center, zoom_start=12)

# Adding a marker at the correct coordinates
folium.Marker(
    [40.7128, -74.0060], # Location New York
    popup="Abuja",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

# If using in a Jupyter notebook, display the map
display(mymap)
mymap.save("abuja.html")
# If running in a standard Python environment, save the map to an HTML file
# mymap.save("mymap.html")






#Lagos Nigeria map.
# use chat gpt to get the country Latitude: Longitude e.g [6.5244, 3.3792]


# import folium
# from IPython.display import display

# # Correcting the longitude for New York (should be negative)
# map_center = [6.5244, 3.3792]
# mymap = folium.Map(location=map_center, zoom_start=12)

# # Adding a marker at the correct coordinates
# folium.Marker(
#    [6.5244, 3.3792],
#     popup="Nigeria",
#     icon=folium.Icon(color="blue", icon="info-sign")
# ).add_to(mymap)

# # If using in a Jupyter notebook, display the map
# display(mymap)
# mymap.save("nigeriamap.html")
# # If running in a standard Python environment, save the map to an HTML file
# # mymap.save("mymap.html")


# for Abuja [9.0765, 7.3986]