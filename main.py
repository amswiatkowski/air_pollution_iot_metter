from time import sleep
import src.airPollutionMetter as airPollutionMetter

def main():
    print('START')
    airPollutionMetter.getMetters()
    print('END')
main()