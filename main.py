from selenium import webdriver
import time
from sys import argv

PATH = argv[1]
driver = webdriver.Chrome(PATH)

driver.get("http://ec2-54-208-152-154.compute-1.amazonaws.com/")


def get_board_size(min_value, max_value):
    return int((max_value - min_value) / 2)


def get_maximum(min_value, max_value):
    return max_value - int((max_value - min_value) / 2)


def get_minimum(min_value, max_value):
    return min_value + int(((max_value - min_value) / 2))


def get_midpoint(min_value, max_value):
    return int((min_value + max_value) / 2)


def get_coin_button(coin_id_value):
    return driver.find_element_by_id(coin_id_prefix + str(coin_id_value))


left_board_id_prefix = "left_"
right_board_id_prefix = "right_"
coin_id_prefix = "coin_"

weigh_button = driver.find_element_by_id("weigh")
reset_button = driver.find_element_by_xpath("//div/div/div[4]/button[@id='reset']")
result_button = driver.find_element_by_id("reset")  # naming is incorrect on this button; should be 'result'

minimum = 0
maximum = 8
board_size = get_board_size(minimum, maximum)
solution = 0

while 1:
    for i in range(0, board_size):
        left_element = driver.find_element_by_id(left_board_id_prefix + str(i))
        left_element.send_keys(str(i + minimum))

        right_element = driver.find_element_by_id(right_board_id_prefix + str(i))
        right_element.send_keys(str(maximum - i))

    weigh_button.click()
    time.sleep(3)

    result_value = result_button.get_attribute("innerText")

    if result_value == "=":
        solution = get_midpoint(minimum, maximum)
        break

    if result_value == "<":
        if (maximum - minimum) == 2:
            solution = minimum
            break
        maximum = get_maximum(minimum, maximum)

    else:
        if (maximum - minimum) == 2:
            solution = maximum
            break
        minimum = get_minimum(minimum, maximum)

    board_size = get_board_size(minimum, maximum)
    reset_button.click()

coin_button = get_coin_button(solution)
coin_button.click()

print("Alert text", driver.switch_to.alert.text, "\n")
time.sleep(3)

driver.switch_to.alert.dismiss()
print("The fake bar is #", solution, "\n")

weighings = driver.find_element_by_class_name("game-info")
print(weighings.get_attribute("innerText"))
