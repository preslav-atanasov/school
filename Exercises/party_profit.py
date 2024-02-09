group_size = int(input())
days = int(input())
coins = 0

total_coins = 0
companions_count = group_size

for day in range(1, days + 1):
    total_coins += 50 - 2 * companions_count  # Earning and spending on food

    if day % 3 == 0:
        total_coins -= 3 * companions_count  # Spending on party water

    if day % 5 == 0:
        total_coins += 20 * companions_count  # Earning from boss monster
        if day % 3 == 0:
            total_coins -= 2 * companions_count  # Additional spending on party day

    if day % 10 == 0:
        companions_count -= 2  # Two companions leave

    if day % 15 == 0:
        companions_count += 5  # Five new companions join
print(f"{companions_count} companions received {int((total_coins / group_size))} coins each")
    