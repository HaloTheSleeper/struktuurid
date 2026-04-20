function solveTSPWithSimulatedAnnealing(cities) {
  const n = cities.length;
  if (n <= 1) return { distance: 0, route: [...Array(n).keys()] };

  function dist(i, j) {
    const dx = cities[i][0] - cities[j][0];
    const dy = cities[i][1] - cities[j][1];
    return Math.hypot(dx, dy);
  }

  function totalDistance(route) {
    let sum = 0;
    for (let i = 0; i < route.length - 1; i++) {
      sum += dist(route[i], route[i + 1]);
    }
    sum += dist(route[route.length - 1], route[0]);
    return sum;
  }

  function randomRoute(size) {
    const route = [...Array(size).keys()];
    for (let i = size - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [route[i], route[j]] = [route[j], route[i]];
    }
    return route;
  }

  function neighbor(route) {
    const next = route.slice();
    const i = Math.floor(Math.random() * next.length);
    let j = Math.floor(Math.random() * next.length);
    while (j === i) j = Math.floor(Math.random() * next.length);
    [next[i], next[j]] = [next[j], next[i]];
    return next;
  }

  let currentRoute = randomRoute(n);
  let currentDistance = totalDistance(currentRoute);

  let bestRoute = currentRoute.slice();
  let bestDistance = currentDistance;

  let temperature = 1000;
  const coolingRate = 0.995;
  const minTemperature = 1e-4;
  const iterationsPerTemp = 100;

  while (temperature > minTemperature) {
    for (let k = 0; k < iterationsPerTemp; k++) {
      const candidateRoute = neighbor(currentRoute);
      const candidateDistance = totalDistance(candidateRoute);

      const delta = candidateDistance - currentDistance;

      if (delta < 0 || Math.random() < Math.exp(-delta / temperature)) {
        currentRoute = candidateRoute;
        currentDistance = candidateDistance;

        if (currentDistance < bestDistance) {
          bestDistance = currentDistance;
          bestRoute = currentRoute.slice();
        }
      }
    }

    temperature *= coolingRate;
  }

  return {
    distance: bestDistance,
    route: bestRoute,
  };
}

const cities = [
  [0, 0],
  [1, 5],
  [5, 2],
  [6, 6],
  [8, 3],
];

const result = solveTSPWithSimulatedAnnealing(cities);
console.log(result.distance);
console.log(result.route);
