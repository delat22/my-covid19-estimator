import math

data = {
    "region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 5,
        "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614
}


def timeEstimate(currentlyInfected, time):
  factor = math.trunc(time/3)
  return currentlyInfected*2**factor

def getTime(duration, figure):
  if duration == 'months':
    return figure*30
  elif duration == 'weeks':
    return figure*7
  else:
    return figure
def estimator(data):
  days = getTime(data['periodType'], data['timeToElapse'])

  currentlyInfected = data['reportedCases']*10
  severeCurrentlyInfected = data['reportedCases']*50

  infectionsByRequestedTime = timeEstimate(currentlyInfected, days)
  severeInfectionsByRequestedTime = timeEstimate(severeCurrentlyInfected, days)



  
  impact = {"currentelyInfected": currentlyInfected, "infectionsByRequestedTime": infectionsByRequestedTime

  }

  severeImpact = {"severeCurrentlyInfected": severeCurrentlyInfected, "severeInfectionsByRequestedTime": severeInfectionsByRequestedTime

  }
  return {"data": data, "impact": impact, "severeImpact": severeImpact} 



