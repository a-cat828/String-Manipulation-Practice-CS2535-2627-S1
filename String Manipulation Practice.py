name = "   aLeX mOrGaN   "
print(name.lower().strip())
status = "WARNING::ENGINE_OVERHEAT::SECTOR_7"
print(status.replace(":", "|").lower().replace("_", " "))
modules = "navigation|life_support|cargo_bay|engine_control"
modules =modules.replace("_", " ").title().split("|")
modules = ", ".join(modules)
print(modules)
readings = "  18,27,35,20  "
readings = readings.strip().split(",")
readings1 = int(readings[0])
readings2 = int(readings[1])
readings3 = int(readings[2])
readings4 = int(readings[3])
Total = readings1 + readings2 + readings3 + readings4
Average = (readings1 + readings2 + readings3 + readings4) / 4
print(Total)
print(Average)
