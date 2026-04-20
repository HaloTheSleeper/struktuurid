function knapsackBranchAndBound(weights, values, capacity) {
  const n = weights.length;
  if (n === 0 || capacity <= 0) return 0;
  if (values.length !== n) {
    throw new Error("weights and values must have the same length");
  }

  const items = weights
    .map((w, i) => ({
      weight: w,
      value: values[i],
      ratio: values[i] / w,
    }))
    .sort((a, b) => b.ratio - a.ratio);

  function getBound(level, currentWeight, currentValue) {
    if (currentWeight >= capacity) return currentValue;

    let bound = currentValue;
    let totalWeight = currentWeight;
    let i = level + 1;

    while (i < n && totalWeight + items[i].weight <= capacity) {
      totalWeight += items[i].weight;
      bound += items[i].value;
      i++;
    }

    if (i < n) {
      const remaining = capacity - totalWeight;
      bound += remaining * items[i].ratio;
    }

    return bound;
  }

  let bestValue = 0;

  function dfs(level, currentWeight, currentValue) {
    if (currentWeight <= capacity && currentValue > bestValue) {
      bestValue = currentValue;
    }

    if (level === n - 1) return;

    const bound = getBound(level, currentWeight, currentValue);
    if (bound <= bestValue) return;

    const nextIndex = level + 1;
    const nextItem = items[nextIndex];

    if (currentWeight + nextItem.weight <= capacity) {
      dfs(
        nextIndex,
        currentWeight + nextItem.weight,
        currentValue + nextItem.value,
      );
    }

    dfs(nextIndex, currentWeight, currentValue);
  }

  dfs(-1, 0, 0);
  return bestValue;
}

const weights = [2, 3, 5, 7];
const values = [30, 30, 50, 70];
const capacity = 10;

console.log(knapsackBranchAndBound(weights, values, capacity));
