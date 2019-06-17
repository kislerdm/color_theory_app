export function hexCut(color) {
  return (color.charAt(0)==="#") ? color.substring(1,7):color;
}
