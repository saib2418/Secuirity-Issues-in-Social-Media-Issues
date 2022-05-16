import csv 

with open("ig_data.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    # print(header)
    val = input("Enter instagram account you want to check: ")
    # print(val)
    for row in reader:
        username = row[0]
        profile_pic = row[3]
        verified = row[4]
        if (val == username or profile_pic == [] or verified == []):
            print("Account is fake!")






# user_media_count - Total number of posts, an account has.
# user_follower_count - Total number of followers, an account has.
# user_following_count - Total number of followings, an account has.
# user_has_profile_pic - Whether an account has a profile picture, or not.
# user_is_private - Whether an account is a private profile, or not.
# user_biography_length - Number of characters present in account biography.
# username_length - Number of characters present in account username.
# username_digit_count - Number of digits present in account username.
# is_fake
