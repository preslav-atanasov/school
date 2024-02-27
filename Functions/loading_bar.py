def loading_bar(percentage):
    percent = percentage
    bar_segments = 10
    full_segments = 0

    if percentage % 10 == 0 and 1 <= percentage <= 100:
        for number in range(1, percentage+1):
            if number % 10 == 0:
                full_segments += 1
                bar_segments -= 1
            percentage -= 1

        fullsymbol = "%" * full_segments
        barsymbol = "." * bar_segments

        if percent == 100:
            print("100% Complete!")
            print(f"[{fullsymbol}{barsymbol}]")

        if percent < 100:
            print("Still loading...")
            print(f"{percent}% [{fullsymbol}{barsymbol}]")
    else:
        print("Please enter a valid percentage (10, 20, 30...)")


loading_bar(percentage=int(input("")))
