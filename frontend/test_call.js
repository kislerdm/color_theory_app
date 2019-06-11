async function getColorType(hex) {
  const url = `https://color-theory-app.dkisler.com/api/type/type/hex?hexcode=${hex}`;

  const response = await fetch(url);

  if (response.ok) {
    return await response.json();
  } else {
    throw new Error("Cannot fetch");
  }
}
