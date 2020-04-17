

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


def estimator(data):

  currentelyInfected = data['reportedCases'] * 10
  severeCurrentlyInfected = data['reportedCases'] * 50

  infectionsByRequestedTime = timeEstimate(data[currentelyInfected], days)
  severeInfectionsByRequestedTime = timeEstimate(data[severeCurrentlyInfected], days)



  
  impact = {"currentelyInfected": currentelyInfected, "infectionsByRequestedTime": infectionsByRequestedTime

  }

  severeImpact = {"severeCurrentlyInfected": severeCurrentlyInfected, "severeInfectionsByRequestedTime": severeInfectionsByRequestedTime

  }
  return {"data": data, "impact": impact, "severeImpact": severeImpact} 

def timeEstimate(currentelyInfected, time):
  factor = math.trunc(time/3)
  return currentelyInfected * 2 ** factor