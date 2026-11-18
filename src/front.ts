import type {Page} from "@shared/instrument";
import {rect, type Frame} from "@shared/surface";

export function marks(page: Page): Frame {
  if (page.caption === "RAIN LIMIT") {
    if (!/^\d+(\.\d+)?%$/.test(page.value)) return [];
    const percent = Math.max(0,Math.min(100,parseFloat(page.value)));
    return [rect("probability",51,10,19,2,"#425965FF"),
      rect("limit",51+Math.round(18*percent/100),7,1,8,"#91DCCBFF")];
  }
  if (!Array.isArray(page.hours)) return [];
  return page.hours.slice(0,8).map((hour,i)=>rect("hour"+i,48+i*3,hour==="slot"?6:9,2,hour==="slot"?9:6,
    hour==="slot"?"#B4F3C1FF":hour==="dry"?"#71B8A2FF":hour==="wet"?"#608DC1FF":"#37434BFF"));
}
