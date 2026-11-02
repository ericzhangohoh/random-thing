# Working Templates

Copy only the templates needed for the current stage into the contest project's owned paths. Replace bracketed fields with actual information; leave unknown values explicitly unknown. A completed form is evidence of a recorded decision, not proof of its correctness.

| Template | Destination / owner | When used |
|---|---|---|
| [Intake](INTAKE.md) | `control/intake.md`, coordinator | Start or material rule/input change |
| [Requirements](REQUIREMENTS.md) | `control/requirements.md`, coordinator | Before G1 and when task interpretation changes |
| [State](STATE.md) | `control/state.md`, coordinator | At milestones, handoffs and before context loss |
| [Task](TASK.md) | `control/tasks/`, coordinator | Before assigning bounded work |
| [Model decision](MODEL_DECISION.md) | `models/decisions/`; accepted decision mirrored by coordinator | Candidate comparison and G2 |
| [Assumptions](ASSUMPTIONS.md) | `models/assumptions.md`, modeler | Modeling and revision |
| [Sources and data](SOURCES_AND_DATA.md) | `research/`, domain-data | Evidence admission and data handoff |
| [Model specification](MODEL_SPEC.md) | `models/`, modeler | Before formal implementation |
| [Experiment](EXPERIMENT.md) | `models/experiments/`, modeler; execution via handoff | Before comparing or validating |
| [Run manifest](run_manifest.json.template) | `runs/<run-id>/manifest.json`, computation | Every accepted numerical run |
| [Claims](CLAIM_EVIDENCE.md) | Proposed by writer/modeler; accepted index in `control/` | G3 and manuscript checks |
| [Review](REVIEW.md) | `qa/`, reviewer | Version-specific independent review |
| [Handoff](HANDOFF.md) | `handoffs/<task-id>/<role>-rNN.md`, worker | Every transfer of responsibility |
| [Change request](CHANGE_REQUEST.md) | Requester's handoff directory | Changing accepted dependencies |
| [AI-use record](AI_USE.md) | Each role's handoff log; coordinator integrates | Throughout actual work |
| [Delivery check](DELIVERY.md) | `qa/` review and `control/` release record | Final exported artifact |

See [worked examples](../examples/README.md) for populated examples. Examples are demonstrations, not computed results for a current contest.
