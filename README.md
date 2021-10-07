# FarmDashboard

## 修改get_data.py
修改function：get_temp()、get_hum()、get_CO2()內的```db.get_datas```

## 修改mushroom.html
1. 上方 ```<img src="{{ url_for('static',filename ='mushroom_0203/2021-05-18.jpg') }}" alt="" id="imageresource"```，修改顯示預設image的路徑
2. 下方JavaScript中，```document.getElementById("imageresource").src```，修改成自己的照片路徑
