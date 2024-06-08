def presenteer(my_dict, totaal):
    for key, value in my_dict.items():
        print(f"{key} : {value} euro")
    print("=" * 25)
    print(f"Totaal : {totaal} euro")
