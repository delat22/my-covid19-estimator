
def estimator(data):
  days = getTime(data['periodType'], data['timeToElapse'])

  currentlyInfected = data['reportedCases']*10
  severeCurrentlyInfected = data['reportedCases']*50

  infectionsByRequestedTime = timeEstimate(currentlyInfected, days)
  severeInfectionsByRequestedTime = timeEstimate(severeCurrentlyInfected, days)



  
  impact = {"currentlyInfected": int(currentlyInfected), "infectionsByRequestedTime": int(infectionsByRequestedTime)

  }

  severeImpact = {"severeCurrentlyInfected": int(severeCurrentlyInfected), "severeInfectionsByRequestedTime": int(severeInfectionsByRequestedTime)

  }
   {"data": data, "impact": impact, "severeImpact": severeImpact}
  return {"data": data, "impact": impact, "severeImpact": severeImpact}

def timeEstimate(currentlyInfected, time):
  factor = time//3
  return currentlyInfected*(2**factor)

def getTime(duration, figure):
  if duration == 'months':
    return figure*30
  elif duration == 'weeks':
    return figure*7
  else:
    return figure