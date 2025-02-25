import folium
import webbrowser

# Create a map centered on Hong Kong
map_hk = folium.Map(location=[22.3193, 114.1694], zoom_start=12, tiles="Cartodb Positron")


# Stamen Watercolor tiles
stamen_layer = folium.TileLayer(
 tiles="https://watercolormaps.collection.cooperhewitt.org/tile/watercolor/{z}/{x}/{y}.jpg",
 attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under CC BY SA.",
 name="Water Color",
 overlay=False).add_to(map_hk)


fg = folium.FeatureGroup(name="Show markers", show=True).add_to(map_hk)
folium.LayerControl().add_to(map_hk)


tooltip = "Click Me!"

# Image of Victoria Peak
vp_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/Hong_Kong_Night_view_from_Victoria_Peak.jpg"


# Empty heart and full heart icon
empty_heart_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/heart.png"
full_heart_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/redheart.png"


# Victoria Peak Pop-Up Content
vp_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Victoria Peak
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{vp_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        The highest point on Hong Kong Island, offering breathtaking views of the skyline
    </p>
</div>
"""


# Victoria Peak marker
folium.Marker([22.2758, 114.1456], popup=folium.Popup(vp_popup_content, max_width=250),
  icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/location%20(1).png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image of Tian Tan Buddha
ttb_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/tian_tan_buddha.jpg"

# Tian Tan Buddha Pop-Up content
ttb_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Tian Tan Buddha
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{ttb_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        The majestic statue on Lantau Island, offers stunning views of the lush mountains
    </p>
</div>
"""

# Tian Tan Buddha marker
folium.Marker(
    [22.2525, 113.9031],
    popup=folium.Popup(ttb_popup_content, max_width=250), icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/location%20(1).png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image of Avenue of Stars
aos_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/avenueofstars.png"

# Avenue of Stars Pop-Up content
aos_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Avenue of Stars
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{aos_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A scenic promenade honoring Hong Kong's cinematic legends along Victoria Harbour
    </p>
</div>
"""

# Avenue of Stars marker
folium.Marker([22.2932, 114.1746], popup=aos_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/location%20(1).png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of Victoria Harbour
vh_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/victoriaharbour.png"

# Victoria Harbour Pop-Up content
vh_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Victoria Harbour
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{vh_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A scenic promenade honoring Hong Kong's cinematic legends along Victoria Harbour
    </p>
</div>
"""

# Victoria Harbour marker
folium.Marker([22.2820, 114.1735], popup=vh_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/location%20(1).png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of Ngong Ping 360
np360_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/npthreesixty.png"

# Ngong Ping 360 Pop-Up content
np360_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Ngong Ping 360
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{np360_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A scenic cable car ride offering panoramic views of Lantau Island’s peaks and coastline
    </p>
</div>
"""

# Ngong Ping 360 marker
folium.Marker([22.2559, 113.9025], popup=np360_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/location%20(1).png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of Wong Tai Sin Temple
wtst_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/wtst.png"

# Wong Tai Sin Temple Pop-Up content
wtst_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Wong Tai Sin Temple
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{wtst_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A vibrant Taoist temple renowned for its prayer-answering traditions in Kowloon
    </p>
</div>
"""

# Wong Tai Sin Temple marker
folium.Marker([22.3424, 114.1936], popup=wtst_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/location%20(1).png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)




# Image URL of Lan Kwai Fong
lkf_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/lankwaifong.png"

# Lan Kwai Fong Pop-Up content
lkf_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Lan Kwai Fong
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{lkf_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A lively nightlife hub packed with bars and eateries in Central Hong Kong
    </p>
</div>
"""

# Lan Kwai Fong marker
folium.Marker([22.2806, 114.1557], popup=lkf_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/blueloca.png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of Nathan Road
nr_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/nathanroad.png"

# Nathan Road Pop-Up content
nr_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Nathan Road
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{nr_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A bustling ‘Golden Mile’ lined with shops and neon lights in Kowloon’s heart
    </p>
</div>
"""

# Nathan Road marker
folium.Marker([22.2950, 114.1719], popup=nr_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/blueloca.png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of Temple Street
ts_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/templestreet.png"

# Temple Street Pop-Up content
ts_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Temple Street
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{ts_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A lively night market buzzing with stalls and street food in Kowloon
    </p>
</div>
"""

# Temple Street marker
folium.Marker([22.3070, 114.1702], popup=ts_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/blueloca.png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of Hollywood Street
hs_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/hollywood.png"

# Hollywood Street Pop-Up content
hs_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Hollywood Street
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{hs_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A historic street famed for antiques and art in Central Hong Kong
    </p>
</div>
"""

# Hollwood Street marker
folium.Marker([22.2832, 114.1528], popup=hs_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/blueloca.png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of Kam's Roast Goose
krg_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/kamsroast.png"

# Kam's Roast Goose Pop-Up content
krg_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Kam's Roast Goose
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{krg_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A Michelin-starred gem serving juicy roast goose and crispy char siu in Wan Chai
    </p>
</div>
"""

#  Kam's Roast Goose marker
folium.Marker([22.2777, 114.1725], popup=krg_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/greenloca.png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of Mammy Pancake
mp_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/mammy.png"

# Mammy Pancake Pop-Up content
mp_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Mammy Pancake
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{mp_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        A tiny stall dishing out crispy, fluffy egg waffles in Tsim Sha Tsui
    </p>
</div>
"""

# Mammy Pancake marker
folium.Marker([22.2986, 114.1721], popup=mp_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/greenloca.png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Image URL of The Chairman
tc_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/tc.png"

# The Chairman Pop-Up content
tc_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        The Chairman
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{tc_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        Elegant Cantonese dining with bold flavors on Wellington Street
    </p>
</div>
"""

# The Chairman marker
folium.Marker([22.2815, 114.1550], popup=tc_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/greenloca.png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)

# Image URL of Hop Yik Tai
hyt_image_url = "https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/hup.png"

# Hop Yik Tai Pop-Up content
hyt_popup_content = f"""
<div style='width: 250px; text-align: center;'>
    <h4 style='font-family: Arial; color: black; margin-bottom: 10px;'>
        Hop Yik Tai
        <img src="{empty_heart_url}" style="width: 16px; height: 16px; cursor: pointer; vertical-align: middle;" onclick="this.src = this.src === '{full_heart_url}' ? '{empty_heart_url}' : '{full_heart_url}'">
    </h4>
    <img src="{hyt_image_url}" width="200px" style='border-radius: 10px;'><br>
    <p style='font-family: Arial; font-size: 12px; color: gray;'>
        Silky cheong fun and street eats in the heart of Sham Shui Po
    </p>
</div>
"""

# Hop Yik Tai marker
folium.Marker([22.3298, 114.1662], popup=hyt_popup_content, icon=folium.CustomIcon("https://raw.githubusercontent.com/zorocubing/Map-of-The-Pearl/main/greenloca.png", icon_size=(30, 30)), tooltip=tooltip).add_to(fg)


# Save to an HTML file and open the file in web browser
map_hk.save("map.html")
webbrowser.open("map.html")


print("Map has been generated! Open map.html to view it")
