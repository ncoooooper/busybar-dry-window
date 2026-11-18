import {marks} from "./front";
import {instrument} from "@shared/instrument";

instrument({
  marks,
  "title": "DRY WINDOW",
  "primary": "Dry Window",
  "accent": "#8AD7C4",
  "cadence": 900000,
  "motion": {enabled:false},
  "setup": "Start companion/serve.py"
});
