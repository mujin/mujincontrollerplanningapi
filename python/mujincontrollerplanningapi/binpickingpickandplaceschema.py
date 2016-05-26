# -*- coding: utf-8 -*-
# Copyright (C) 2016 MUJIN Inc
__author__ = 'Denys Kanunikov'

from . import _
from . import postcycleexecutionconfigschema

#
# Properties has to be in alphabetic order by name!!!
#

jointValuesSchema = {
    "title": _("Joint values of the robot"),
    "description": _("mm or degrees. Need to specify values for all joints."),
    "type": "array",
    "items": {
        "description": _("Joint value of the robot"),
        "type":"number",
        "default":0
    },
    "minItems": 0,
    "maxItems": 7, # TODO: think about better definition of joint values, by getting value from the robot parameters somehow
    "additionalItems": False,
    "format": "mujin.robotJointValues",
}

ikParamNamesSchema = {
    "title": _("Ik parameter names"),
    "description": _("Names of the destination ik parameters robot will go to. should be in the format instobjectname/ikparamname"),
    "type": "array",
    "items": {
        "title": _("Destination ik parameter name"),
        "description": _("Should be in the format instobjectname/ikparamname"),
        "type":"string",
        "default": "",
    },
    "additionalItems": False,
}

destGoalSchema = {
    # "title": _("Destination goal"),
    "description" : _("Destination goal dictionary. If 'jointvalues' is specified ikparamnames will be ignored"),
    "type": "object",
    "properties":{
        "jointvalues": dict(jointValuesSchema.items() + {"title": _("Joint values of the robot")}.items()),
        "ikparamnames": ikParamNamesSchema,
        "validGraspSetName": {
            "title": _("The set of grasps valid for that goal"),
            "type": "string",
        },
        "name":{
            "title": _("Name"),
            "type":"string",
        },
    },
}

destGoalsSchema = {
    "title": _("Destination goals"),
    "description": _("list of dictionaries where each dictionary contains the goal description. A goal contains: ikparamnames or jointvalues, validGraspSetName(optional), name(optional)."),
    "type": "array",
    "items": destGoalSchema,
    "additionalItems": False,
    "tags": ["basic", "si", "system"]
}

translationOffsetSchema = {
    "title": _("Translation offset"),
    "description": _("mm, x,y,z"),
    "type": "array",
    "additionalItems": False,
    "minItems": 3,
    "maxItems":3,
    "items":[
        {"title": _("x"), "type":"number", "default":0 },
        {"title": _("y"), "type":"number", "default":0 },
        {"title": _("z"), "type":"number", "default":0 }
    ]
}


binpickingConfigSchema = {
    "title": _("Binpicking parameters configurations"),
    "description": _("Different parameters to configure binpicking pick and place cycle."),
    "type": "object",
    "properties": {
        #
        # basic
        #
        "alwaysPlanOutOfOcclusion": {
            "title": _("Always plan out of camera occlusion"),
            "description": _("If true plans out of camera occlusion when execution unexpectedly stopped (i.e. piece lost)."),
            "type": "integer",
            "enum": [0,1],
            "tags":["basic", "si", "motion"]
        },
        "approachCurrentExceedThresholds":{
            "title": _("Approach current exceed thresholds"),
            "description": _("Absolute current thresholds that should not exceed by joints"),
            "type": "array",
            "minItems": 0,
            "maxItems": 7,
            "items" : {
                "description": "J1, J2, J3, J4, J5, J6, J7",
                "type": "number",
                "default": 1,
                "min": 0.0,
                "max": 1.0,
            },
            "additionalItems": False,
            #     },
            #     {"type": "null"}
            # ],
            "tags":["medium", "si", "motion"],
        },
        "approachCurrentExceedThresholdsDelta":{
            "title": _("Approach current exceed thresholds delta"),
            "description": _("values in [0,1] that check if any of the currents exceed the difference between the start current thresholds (at torqueCheckStartTime) and the current ones. If they do, then will return torque error. Do the check after torqueCheckStartTime."),
            # "anyof":[{
            "type": "array",
            "minItems": 0,
            "maxItems": 7,
            "items" : {
                "description": "J1, J2, J3, J4, J5, J6, J7",
                "type": "number",
                "default": 0.5,
                "min": 0.0,
                "max": 1.0,
                },
            "additionalItems": False,
            # },
            #     {"type": "null"}
            # ],
            "tags":["medium", "si", "motion"]
        },
        "approachoffset": {
            "title": _("Approach grasp offset"),
            "description": _("mm"),
            "type": "number",
            "tags":["basic", "si", "motion"]
        },
        "checkForEndEffectorLowerThanGraspDist": { 
            "title": _("Check for end-effector distance lower than grasp"),
            "description": _("mm, distance threshold (in mm) for the max distance of ee_translation-tool_translation along the vector oriented toward the container opening (usually +z)."),
            "type": "number",
            "minimum": 0,
            "default": 0.0,
            "tags":["si", "motion", "medium"]
        },
        "checkObstacleNames": { 
            "title": _("Check extra obstacle names"),
            "description": _("Extra obstacle names that represent dynamic data in the destination. Have to wait for all the obstacles to be in the environment before robot can start planning."),
            "type": "array",
            "items": {
                "description": _("Body name"),
                "type":"string",
                "default": "",
                "format": "mujin.bodyName",
            },
            "tags":["si", "system", "advanced"],
            "additionalItems": False,
        },
        "checkOverlapRobotLinkName": {
            "title": _("Check overlap robot link name"),
            "description": _("When grasping, use this link to check the overlap area"),
            "type": "string",
            "tags":["si", "motion", "medium"]
        },
        "constraintToolDirection": {
            "title": _("Constraint tool parameters"),
            "description": _("(toolx, tooly, toolz, globalx, globaly, globalz, angle), constrain the tool to be within a cone in a global direction. toolxyz is in the tool coordinate systems, globalxyz is in the global coordinate system, angle constraints how much the tool direction can deviate from the global direction."),
            "type": "array",
            "minItems": 7,
            "maxItems": 7,
            "items" : [
                {
                    "title": _("toolx"),
                    "description": _("toolx"),
                    "type": "number",
                    "default": 0
                },
                {
                    "title": _("tooly"),
                    "description": _("tooly"),
                    "type": "number",
                    "default": 0
                },
                {
                    "title": _("toolz"),
                    "description": _("toolz"),
                    "type": "number",
                    "default": 0
                },
                {
                    "title": _("globalx"),
                    "description": _("globalx"),
                    "type": "number",
                    "default": 0
                },
                {
                    "title": _("globaly"),
                    "description": _("globaly"),
                    "type": "number",
                    "default": 0
                },
                {
                    "title": _("globalz"),
                    "description": _("globalz"),
                    "type": "number",
                    "default": 0
                },
                {
                    "title": _("angle"),
                    "description": _("angle"),
                    "type": "number",
                    "default": 0
                },
            ],
            "additionalItems": False,
            "tags":["si", "motion", "basic"]
        },
        "constraintToolOptions": {
            "title": _("Constraint tool options"),
            "description": _("""options that control when constraining the tool is applied.
            If 1, then only check the destination at the grasp goal pair
            If 2, then grasp/destination IK should filter
            If 8, then the final position (initial of the next cycle) of the robot should satisfy the constraints
            If 16, then jitterer should always satisfy the constraints. If not set, then jitter satisfies the constraints depending on the usage. Ie if 16 is enabled, then use the constrained jitterer when the part is grabbed.
            If 32, then RRT when part is grabbed should satisfy the constraints
            If 64, then RRT when part is not grabbed should satisfy the constraints"""),
            "type": "integer",
            "minimum": 0,
            "default": 0x23,
            "tags":["motion", "basic", "si"]
        },
        "cycledests": {
            "title": _("Cycle destination repeats"),
            "description": _("Max number of times to repeat the destikparamnames, 0 means infinite repeat"),
            "type": "integer",
            "minimum": 0,
            "default":1,
            "tags":["advanced", "system", "si"]
        },
        "debuglevel": { 
            "title": _("Debug level"),
            "type": "integer",
            "minimum": 0,
            "default":4,
            "tags":["dev", "basic", "system"]
        },
        "deletetarget": { 
            "title": _("Is delete target"),
            "description": _("0: do not delete. 1: delete the target."),
            "type": "integer",
#            "enum": [0,1,2],
            "enum": [0,1],
            "tags":["basic", "si", "target"]
        },
        "deleteTargetFromSourceContainer": { 
            "title": _("Is delete target from source container"),
            "description": _("0: do not delete target after it is picked up until the next detection update. 1: delete the target after it is picked up."),
            "type": "integer",
            "enum": [0,1],
            "default": 0,
            "tags":["advanced", "si", "target"]
        },
        "deletetargetonocclusion": { 
            "title": _("Delete targets on occlusion"),
            "description": _("if True and robot is initially occluding the container, then delete all the targets and wait for vision to repopulate"),
            "type": "boolean",
            "default": True,
            "tags":["medium", "si", "target"]
        },
        "deleteTargetDestInfo":{
            "title": _("Target destination delete info"),
            "description": _("a dict specifying extra dests to aim for when planning. If robot does pick up from them, then robot will delete the target and not increase the goal index. This allows parts that are not placable in the original goals to be put somewhere for later processing. The dict has keys: destikparamnames, validGraspSetName, moveToFinishPositionAtEnd"),
            "type": "object",
            "properties": {
                "destikparamnames": ikParamNamesSchema,
                "intermediatedestname":{
                    "title": _("Intermediate destination names"),
                    "description": _("intermediate destination names of goals, should be in format: instobjectname/ikparamname"),
                    "type": "string",
                },
                "validGraspSetName":{
                    "title": _("Valid grasp set name for the goal"),
                    "type": "string"
                },
            },
            "tags": ["medium", "si", "target"],
        },
        "deleteTargetsOnPieceLost": { 
            "title": _("Is delete targets on piece lost"),
            "description": _("if True, will delete the all computed target results and wait for new ones to come (via the vision system)"),
            "type": "boolean",
            "tags":["medium", "si", "target"]
        },
        "departoffsetdir": {
            "title": _("Depart destination direction offset"),
            "description": _("mm (x,y,z), depart direction offset after releasing a target"),
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items" :[
                {"title": _("x"), "type":"number", "default":0 },
                {"title": _("y"), "type":"number", "default":0 },
                {"title": _("z"), "type":"number", "default":0 }
            ],
            "additionalItems": False,
            "tags":["motion", "basic", "si", "dest"]
        },
        "destApproachAccel": {
            "title" : _("Destination approach maximum acceleration"),
            "description" : _("mm/s^2"),
            "type": "number",
            "default": 1500,
            "tags":["motion", "si", "basic"]
        },
        "destApproachDecel": {
            "title": _("Destination approach maximum deceleration"),
            "description": _("mm/s^2,"),
            "type": "number",
            "default": 1500,
            "tags":["motion", "si", "basic"]
        },
        "destapproachoffsetdir": {
            "title": _("Destination approach offset direction"),
            "description": _("mm (x,y,z)"),
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items" :[
                {"title": _("x"), "type":"number", "default":0 },
                {"title": _("y"), "type":"number", "default":0 },
                {"title": _("z"), "type":"number", "default":0 }
            ],
            "additionalItems": False,
            "tags":["motion", "si", "basic"]
        },
        "destapproachoffsetintool":{
            "title": _("Destination approach offset in the tool coordinate system"),
            "description": _("if True then destapproachoffsetdir is in the tool coordinate system"),
            "type": "boolean",
            "default": False,
            "tags":["motion", "si", "basic"]
        },
        "destApproachSpeed": {
            "title": _("Destination maximum approach speed"),
            "description": _("mm/s"),
            "type": "number",
            "default": 1000.0,
            "tags":["motion","si", "basic"]
        },
        "destcoordtype": {
            "title": _("Destination coordinate type"),
            "description": _("coordinate system type of the destination. can be 'target', 'tool'"),
            "type": "string",
            "enum": ["tool", "target"],
            "tags":["motion", "si", "basic"]
        },
        "destDepartAccel": {
            "title" : _("Destination depart maximum acceleration"),
            "description" : _("mm/s^2, "),
            "type": "number",
            "default": 1600,
            "tags":["motion", "si", "basic"]
        },
        "destDepartDecel": {
            "title": _("Destination depart maximum deceleration"),
            "description": _("mm/s^2, "),
            "type": "number",
            "default": 1600,
            "tags":["motion", "si", "basic"]
        },
        "destDepartSpeed": {
            "title": _("Destination depart maximum speed"),
            "description": _("mm/s"),
            "type": "number",
            "default": 1600.0,
            "tags":["motion", "si", "basic"]
        },
        "destdepartoffsetdir": {
            "title": _("Destination depart offset direction"),
            "description": _("mm (x,y,z)"),
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items" :[
                {"title": _("x"), "type":"number", "default":0 },
                {"title": _("y"), "type":"number", "default":0 },
                {"title": _("z"), "type":"number", "default":0 }
            ],
            "additionalItems": False,
            "tags":["motion", "si", "basic"]
        },
        "destdepartoffsetintool": {
            "title": _("Destination depart offset in tool coordinate system"),
            "description": _("If true then destination depart offset is computed in the tool coordiante system"),
            "type": "boolean",
            "default": False,
            "tags":["motion", "si", "advanced"]
        },
        "destFilterByTargetOrientationThresh":{
            "title": _("Destination filter target orientation"),
            "description": _("deg, enabled if destcoordtype==target. an angle is used to filter destinations such that they only allow targets in the source container that are oriented around the container's up axis. The minimum rotation angle between the source and destination target poses (once they are normalized by the in-plane rotatation) is thresholded by this value. if less than 0, then invalid. angle in degrees."),
            "type": "number",
            "tags":["motion", "advanced", "si"]
        },
        "destGoals":destGoalsSchema,
        "destTargetValidationJitterDist":{
            "title": _("Destination target valid jitter distance"),
            "description": _("mm, if a target at the destination is in collision, then can jitter by this distance so that a new collision-free goal could be used instead. This is used when a destination point cloud is used to pack items."),
            "type": "number",
            "default": 0.0,
            "tags":["motion", "advanced", "si"]
        },
        # "disablebodiesforcontainer":{
        #     "title": _("Bodies to disable for container"),
        #     "description": _("key value pairs of container names and bodies that should be disabled when picking up from that container"),
        #     "type": "object",
        #     "properties":{
        #         },# TODO: provide a ui for editing dictionaries like this
        #     "tags": ["dev", "system"],
        # },
        # "enablebodiesforcontainer":{
        #     "title": _("Bodies to enable for container"),
        #     "description": _("key value pairs of container names and bodies that should be disabled when picking up from that container"),
        #     "type": "object",
        #     "properties":{
        #         },# TODO: provide a ui for editing dictionaries like this
        #     "tags": ["dev"],
        # },
        "ensureTargetDestCollisions": {
            "title": _("Ensure target destination collisions"),
            "description": _("if 1 then will re-add any placed targets again before continuing to plan. this option exists for some ode collision checking when boxes are inside boxes (squse splitroll0)"),
            "type": "integer",
            "enum": [0,1],
            "tags":["motion", "dev", "medium"]
        },
        "executionFilterFactorWhenGrabbing": {
            "title": _("Execution filter factor grabbing an item"),
            "description": _("parameter to use for multiplying the filterconst in FilterRobotTrajectory. if None will decide depending on executeparameters.constraintToolDirection"),
            "type": "number",
            "minimum": 0.01,
            "maximum": 1.0,
            "default": 0.4,
            "tags":["motion", "si", "medium"]
        },
        "executethread": {
            "title": _("Use execute thread"),
            "type": "boolean",
            "default": True,
            "tags":["dev", "system"]
        },
        "feedbackDestJointThreshold": { 
            "title": _("Feedback Joint Workspace Threshold"),
            "description": _("deg/mm, how many deg/mm each joint has to be from the commanded dest (release) position to declare that it is in at the destination. The smaller the value, the more accurate the robot will be, but will be slower. Used with feedbackDestWorkspaceThreshold."),
            "type": "number",
            "minimum": 1.0,
            "tags":["motion", "si", "medium"]
        },
        "feedbackDestWorkspaceThreshold": { 
            "title": _("Feedback Dest Workspace Threshold"),
            "description": _("mm, how many mm the real tooltip position has to be from the commanded dest (release) position to declare that it is in at the destination. The smaller the value, the more accurate the robot will be, but will be slower. Used with feedbackDestJointThreshold."),
            "type": "number",
            "minimum": 1.0,
            "tags":["motion", "si", "medium"]
        },
        "feedbackGraspJointThreshold": { 
            "title": _("Feedback Grasp Joint Threshold"),
            "description": _("deg/mm, how many deg/mm each joint has to be from the commanded grasp joint values to declare that it is at the grasp. The smaller the value, the more accurate the robot will be, but will be slower. Used with feedbackGraspWorkspaceThreshold."),
            "type": "number",
            "minimum": 1.0,
            "tags":["motion", "si", "medium"]
        },
        "feedbackGraspWorkspaceThreshold": { 
            "title": _("Feedback Grasp Workspace Threshold"),
            "description": _("mm, how many mm the real tooltip psition has to be from commanded grasp position to declare that it is at the grasp. The smaller the value, the more accurate the robot will be, but will be slower. Used with feedbackGraspJointThreshold."),
            "type": "number",
            "minimum": 1.0,
            "tags":["motion", "si", "medium"]
        },
        # "externalCollisionIO":{
        #     "title": _("External collision IO signals mapping"),
        #     "description": _("i.e. [['sourcecontainer','notCollidingSourceContainer'], ['destcontainer','notCollidingExternalDevices2']]"),
        #     "type": "array",
        #     "items" : {
        #         "description": "(bodyname, externalCollisionSignalName)",
        #         "type":"array",
        #         "items": "string",
        #         "minItems": 2,
        #         "maxItems":2,
        #         "additionalItems": False,      
        #         },
        #     "tags": ["dev"],
        # },
        "finalPlanMode": {
            "title": _("Final plan mode"),
            "description": _("The mode to compute the final plan. if empty, do not do any final plan for each cycle, the robot stops after the dest depart. If 'cameraocclusion', then make sure robot is away from the camera occlusion. If 'config', then plan for robotRecoveryPosition."),
            "type": "string",
            "enum":["none", "cameraocclusion", "config"],
            "tags":["motion", "basic", "si"]
        },
        "graspApproachAccel": {
            "title" : _("Grasping approach maximum acceleration"),
            "description" : _("mm/s^2"),
            "type": "number",
            "default": 400,
            "tags":["motion", "si", "basic", "grasp"]
        },
        "graspApproachDecel": {
            "title": _("Grasping approach maximum deceleration"),
            "description": _("mm/s^2"),
            "type": "number",
            "default": 400,
            "tags":["motion", "si", "basic", "grasp"]
        },
        "graspApproachSpeed": {
            "title": _("Grasp approach maximum speed"),
            "description": _("mm/s"),
            "type": "number",
            "default": 1600.0,
            "tags":["motion", "si", "basic", "grasp"]
        },
        "graspDepartAccel": {
            "title" : _("Grasp depart maximum acceleration"),
            "description" : _("mm/s^2, "),
            "type": "number",
            "default": 1000,
            "tags":["motion", "si", "basic", "grasp"]
        },
        "graspDepartDecel": {
            "title": _("Grasp depart maximum deceleration"),
            "description": _("mm/s^2, "),
            "type": "number",
            "default": 1000,
            "tags":["motion", "si", "basic", "grasp"]
        },
        "graspDepartSpeed": {
            "title": _("Grasp depart maximum speed"),
            "description": _("mm/s"),
            "type": "number",
            "default": 1600.0,
            "tags":["motion", "si", "basic", "grasp"]
        },
        "graspsetname":{
            "title": _("Grasp set name"),
            "description": _("Name of the grasp set to use for picking"),
            "type": "string",
            "tags":["basic", "grasp", "si"]
        },
        "graspFilterByApproachOrientationThresh":{
            "title": _("Grasp filter approach orientation threshold"),
            "description": _("degrees, an angle is used to filter grasps such that they only allow approaches in the source container that are oriented around the container's up axis given this threshold. if less than 0, then invalid."),
            "type": "number",
            "default": -1,
            "tags":["motion", "advanced", "si"]
        },
        "graspTimeLimit":{
            "title": _("Grasp time limit"),
            "description": _("max time to spend on computing one grasp for one target. 0 means infinite"),
            "type": "number",
            "default": 0.0,
            "tags":["motion", "medium", "grasp", "si"]
        },
        "gripperIODepartCheckStartTime":{
            "title": _("Depart Check Grasp Start Time"),
            "description": _("The time after chucking a target object to start checking if the object was released or not."),
            "type": "number",
            "default": 0.5,
            "tags":["motion", "medium", "grasp", "si"]
        },
        "maxAcceptedDestPlanTrajTime":{
            "title": _("Max Accepted Dest Plan Traj Time"),
            "description": _("if > 0, then will only accept dest plans that are faster than this limit."),
            "type": "number",
            "default": 0.0,
            "tags":["motion", "medium", "grasp", "si"]
        },
        "ignoreDynamicObstaclesInGraspDepart": {
            "title": _("Ignore dynamic obstacles in grasp depart"),
            "description": _("If true, will ignore any dynamic obstacles when departing after grasping"),
            "type": "boolean",
            "default": True,
            "tags":["dev", "grasp", "basic"]
        },
        "iksolverfreeincprismatic": {
            "title": _("IkSolver prismatic free inc"),
            "description": _("mm, when the IK solution requires less DOF than the number of joints of the robot, have to sample the rest of the robot's prismatic axes with this sampling step."),
            "type": "number",
            "default": 0.01,
            "tags":["motion", "advanced", "si"]
        },
        "iksolverfreeincrev": {
            "title": _("IK revolute free increment "),
            "description": _("rad, when the IK solution requires less DOF than the number of joints of the robot, have to sample the rest of the robot's revolute axes with this sampling step."),
            "type": "number",
            "default": 0.1,
            "tags":["motion", "advanced", "si"]
        },
        "iktimelimit": {
            "title": _("IK search time limit"),
            "description": _("the timelimit in microseconds to compute IK solutions until system starts the planning. If no IK solution are computed by this time, then system will wait until at least one pair is computed, or everything is exhausted."),
            "type": "number",
            "minimum": 0.1,
            "default": 2.0,
            "tags":["medium", "motion", "si"]
        },
        "isStopOnPieceLost": { 
            "title": _("Stop on piece lost"),
            "description": _("If True stops the cycle execution if the piece is lost and raise an error"),
            "type": "boolean",
            "default": False,
            "tags":["basic", "si", "system"]
        },
        "linearSmoothingIterations": { 
            "title": _("Linear smoothing iterations "),
            "description": _("How many iterations used for linear smoothing"),
            "type": "integer",
            "minimum": 0,
            "default": 100,
            "tags":["motion", "si", "advanced"]
        },
        "logFailedTargetTimeout": { 
            "title": _("Failed target log timeout"),
            "description": _("seconds, if log entry is a failure, then continue ignoring the part for this many seconds"),
            "type": "number",
            "minimum": 0,
            "tags":["medium", "si", "target"]
        },
        "logPickupTargetTimeout": { 
            "title": _("Pick up target timeout"),
            "description": _("seconds, if a part has been picked up before at a particular location and it is observed again (ie UpdateObjects sets it again). Then if the part was picked up within logPickupTargetTimeout, then picking system will ignore it. If the part was picked up before that, then picking system will treat it as a new part. Usually this is set as **2x** the time between UpdateObjects calls."),
            "type": "number",
            "minimum": 0,
            "default": 30,
            "tags":["medium", "si", "target"]
        },
        "maxDestIkSolutions": { 
            "title": _("Maximum destination IK solutions"),
            "description": _("The maximum IK solutions to have per destiantion before system gives up and tries something else. If 0, then compute all solutions"),
            "type": "integer",
            "minimum": 0,
            "default": 20,
            "tags":["motion", "medium", "system", "si"]
        },
        "maxGraspIkSolutions": { 
            "title": _("Maximum grasping IK solutions"),
            "description": _("The maximum IK solutions to have per target before system gives up and tries something else. If 0, then compute all solutions"),
            "type": "integer",
            "minimum": 0,
            "default": 20,
            "tags":["motion", "medium", "si", "system"]
        },
        "maxFinalPlanIgnoreCount":{
            "title": _("Max final plan ignore count"),
            "description": _("max number of times final plan can be ignored"),
            "type": "integer",
            "default": 0,
            "tags":["motion", "medium", "si"]
        },
        "maxFinalPlanIgnoreMinTargets": {
            "title": _("Max final plan ignore minimum targets"),
            "description": _("minimum number of targets to have before can start to ignore the final plan mode"),
            "type": "integer",
            "default": 6,
            "tags":["motion", "advanced", "si"]
        },        
        "maxGraspIkSolutionsPerGrasp":{
            "title": _("Maximum ik solutions per grasp"),
            "description": _("max grasp solutions allowed per grasp. If 0, then infinite"),
            "type": "integer",
            "default": 10,
            "tags":["motion", "medium", "si", "grasp"]
        },
        "maxjitter": {
            "title": _("Max jitter"),
            "description": _("rad/m, When jittering out of obstacles, the max deviation of any joint"),
            "type": "number",
            "tags":["dev", "advanced", "motion"]
        },
        "maxjitterbias": {
            "title": _("Max jitter bias direction"),
            "description": _("mm, When jittering, try to bias the tool in a specific direction. For example if (0, 0, 100), then the tool will be bias to move up to 100mm on the z axis"),
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items" :[
                {"title": _("x"), "type":"number", "default":0 },
                {"title": _("y"), "type":"number", "default":0 },
                {"title": _("z"), "type":"number", "default":0 }
            ],
            "additionalItems": False,
            "tags":["dev", "advanced", "motion"]
        },
        "maxjitteriters": {
            "title": _("Max jitter iterations"),
            "description": _("The number of tries for jittering out of collisoin before giving up."),
            "type": "integer",
            "tags":["dev", "motion", "advanced"]
        },
        "maxjitterlinkdist": {
            "title": _("Max jitter link dist"),
            "description": _("mm, When jittering, the max distance any link on the robot can move."),
            "type": "number",
            "tags":["dev", "advanced", "motion"]
        },
        "maxLinearFailuresForTargetGrasp":{
            "title": _("Maximum linear failure to grasp target"),
            "description": _("sometimes the grasp depart can fail if the target is still in collision with other objects, in that case all grasp departs will fail"),
            "type": "integer",
            "default": 4,
            "tags":["motion", "medium", "si"]
        },        
        "maxManipAccel": { 
            "title": _("Maximum manipulator acceleration"),
            "description": _("mm/s^2, if != 0, then constrain the manipulator's max accel"),
            "type": "number",
            "minimum": 0,
            "default": 0,
            "tags":["motion", "si", "transfer", "basic"]
        },
        "maxManipSpeed": { 
            "title": _("Maximum manipulator speed"),
            "description": _("mm/s, if != 0, then constrain the manipulator's max speed"),
            "type": "number",
            "minimum": 0,
            "default": 0,
            "tags":["motion", "si", "transfer", "basic"]
        },
        "maxNumConsecutivePieceLost": {
            "title": _("Max number of consecutive piece lost"),
            "description": _("if we lost piece this amount of items in a row, request for container change"),
            "type": "integer",
            "minimum" : 0,
            "tags":["basic", "si", "system"]
        },
        "maxNumPlanningFailedIterations":{
            "title":_("Max num planning failed iterations"),
            "description":_("max number of planning iterations to fail until the system gives up"),
            "type":"integer",
            "minimum":0,
            "default":5,
            "tags":["advanced","si"]
        },
        "maxTorqueMultForApproach": { 
            "title": _("Maximum torque multiplication for approach"),
            "description": _("the percentage of current to limit from maximum when grasp approaching. if 1, then disable"),
            "type": "number",
            "minimum": 0,
            "default": 0.4,
            "maximum": 1.0,
            "tags":["motion", "grasp", "si", "medium"]
        },
        "maxTorqueMultForDestApproach": { 
            "title": _("Maximum torque multiplication for destination approach"),
            "description": _("the percentage of current to limit from max when dest approaching. if 1, then disable"),
            "type": "number",
            "minimum": 0,
            "default": 1.0,
            "maximum": 1.0,
            "tags":["motion", "grasp", "si", "medium"]
        },
        "minGraspDepartCompleteRatio": {
            "title": _("Minimum grasp depart complete ratio"),
            "description": _("controls the percentage of the grasp depart trajectory that the robot needs to minimally achieve in order to move on. This would be used when grasp depart has to be big sometimes, but not always. By default it is 1."),
            "type": "number",
            "minimum": 0,
            "default": 1.0,
            "maximum": 1.0,
            "tags":["motion", "advanced", "grasp", "si"]
        },
        "minLinkOverlapXYSurfaceRatio": {
            "title": _("MinLinkOverlapXYSurfaceRatio"),
            "description": _("default 0.35, when grasping, how much a link's OBB's area projected on the link's XY surface overlaps with the target object's OBB. the link used is sCheckOverlapLinkName"),
            "type": "number",
            "tags":["si", "motion", "advanced"]
        },
        "moveStraightMode": {
            "title": _("Move straight mode"),
            "description": _("default: '6d', the move straight mode. If empty, then robot uses all joints to plan for with respect to the grasp's ik type. If 'all6d', then robot uses all joints to plan for with Transform6D ik type (ie hand orientation doesn't change). If 'min6d', then robot uses the 6 joints to plan for with Transform6D ik type (ie 7DOF arm will move without changing hand orientation)."),
            "type": "string",
            "default": "6d",
            "tags":["dev", "motion", "advanced"]
        },
        "movetodestination": {
            "title": _("Enable move to destination"),
            "description": _("If 1, then robot will place a part in the destination after picking up. If false, then robot will stop the cycle after picking up."),
            "type": "integer",
            "enum": [0,1],
            "tags":["si", "motion", "basic"]
        },
        "neighOverlapThresh": {
            "title": _("Neighbour overlap threshold"),
            "description": _("Max overlap a target can have before robot gives up trying to grasp it"),
            "type": "number",
            "default": 0.4,
            "minimum":0.0,
            "maximum": 1.0,
            "tags":["si", "motion", "advanced"]
        },
        "neighTargetThresh": {
            "title": _("Neighbour target threshold"),
            "description": _("a threshold for position of target objects to determine if they are the same object or not (depends on the vision system, so parameter has to be tweaked)"),
            "type": "number",
            "default":25,
            "tags":["si", "advanced", "motion"]
        },
        "numTargetsToPlace":{
            "title": _("Number of targets to place"),
            "description": _("the number of parts to place in the destination. picked up failures do not count. If 0, then will continue going until cycledests and destikparamnames have been all exhausted. Otherwise will only pick up these parts and stop the pick and place loop."),
            "type": "integer",
            "default":0,
            "tags":["dev", "medium", "system"]
        },
        "numThreads":{
            "title": _("Threads number"),
            "description": _("Number of threads to be used for planning"),
            "type": "integer",
            "default":4,
            "tags":["dev", "system", "basic"]
        },
        "passOnDropAtDestinationNames": {
            "title": _("Pass on drop at destination names"),
            "description": _("List of dest target object names in the environment. if part is dropped above any of these objects's aabbs, then part will be declared as success. By default it is empty"),
            "type": "array",
            "items": {
                "description": _("Body name"),
                "type":"string",
                "default": "",
                "format": "mujin.bodyName",
            },
            "tags":["advanced", "transfer", "grasp", "si"],
            "additionalItems": False,
        },
        "pickFailureDepartRetryNum": { 
            "title": _("Pick failure retry number"),
            "description": _("how many times to retry if failed to pick up. each time is a different direction. 0 means no retries"),
            "type": "integer",
            "minimum": 0,
            "tags":["motion", "medium", "si", "system"]
        },
        "pickFailureDepartRetryWidth": {
            "title": _("Pick failure depart retry width"),
            "description": _("mm, When gripper fails to grab the body, departs a litle and goes back to the body with a small offset."),
            "type": "number",
            "minimum": 0,
            "tags":["motion", "medium", "si"]
        },        
        "postCycleExecution": postcycleexecutionconfigschema.postCycleExecutionConfigSchema,
        "randomBoxInfo":{
            "title": _("Random box info"),
            "description": _("info structure for maintaining grasp parameters for random box picking. Used when picking up randomized boxes (targetIsRandomBox is True), Keys are: usefaces, facepriorities, boxDirAngle, toolTranslationOffsets"),
            "type": "object",
            "properties": {
                "usefaces": {
                    "title": _("Use face"),
                    "description": _("List of faces of the box used to pick it up"),
                    "type":"array",
                    "minItems": 1,
                    "maxItems": 3,
                    "items": {"type": "string", "enum": ['px', 'py', 'pz']},
                    "additionalItems": False,
                },
                "facepriorities": {
                    "title": _("Face pickup priorities"),
                    "description": _("priorities of the faces to pick up the box. In the same order as usefaces"),
                    "type":"array",
                    "items": {"type":"number"},
                    "additionalItems": False,
                },
                "boxDirAngle": {
                    "title": _("Max box direction angle"),
                    "description": _("degrees, max angle of the tool to the box surface that is allowed for pickup."),
                    "type": "number",
                },
                "toolTranslationOffsets":{
                    "title": _("Tool translation offsets"),
                    "description": _("mm, (x,y,z)"),
                    "type":"array",
                    "items": translationOffsetSchema,
                    "additionalItems": False,
                },                
            },
            "tags": ["advanced", "si", "system", "target"],
        },
        "robotCycleStartPosition": dict(jointValuesSchema.items() + {"title": _("Robot cycle start position"), "tags": ["si", "motion", "medium"]}.items()),
        "robotFinishPosition": dict(jointValuesSchema.items() + {"title": _("Robot finish position"), "tags": ["si", "motion", "medium"]}.items()),
        "robotRecoveryPosition": dict(jointValuesSchema.items() + {"title": _("Robot recovery position"), "tags": ["si", "motion", "medium"]}.items()),
        "savetrajectorylog": {
            "title": _("Save trajectory log"),
            "description": _("0 or 1"),
            "type": "integer",
            "default":1,
            "enum": [0,1],
            "tags":["dev", "basic", "system"]
        },
        "skipCollidingDests": {
            "title": _("Is skip colliding destinations"),
            "description": _("if True then will skip any colliding destinations from being considered in the loop"),
            "type": "boolean",
            "default": False,
            "tags":["medium", "si", "system"]
        },
        "smootheriterations": { 
            "title": _("Smoother iterations"),
            "description": _("number of iterations to smooth in parabolic smoother"),
            "type": "integer",
            "minimum": 0,
            "default": 160,
            "tags":["motion", "advanced", "si"]
        },
        "smoothingStepLength": { 
            "title": _("Smoothing step length"),
            "description": _("number of iterations to smooth in parabolic smoother"),
            "type": "number",
            "minimum": 0,
            "default": 0.1,
            "tags":["motion", "advanced", "si"]
        },
        "sourcecameranames": {
            "title": _("Source camera names"),
            "description": _("list of cameras names for doing detection inside the source container. Each camera name is in theformat of kinbody_name/attached_sensor_name. Overwritten by first layer value!"),
            "type": "array",
            "items": {
                "description": _("Name of the camera body in the environment"),
                "type":"string",
                "default": "",
                "format": "mujin.bodyName",
            },
            "additionalItems": False,
            "tags": ["basic", "si", "system", "noui"]
        },
        "sourcecontainername":{
            "title": _("Source container name"),
            "type": "string",
            "format": "mujin.bodyName",
            "tags": ["basic", "si", "system", "noui"],
        },
        "sourceDestTargetOrientationPenalty": {
            "title": _("SourceDestTargetOrientationPenalty"),
            "description": _("value multipled by the rotational angle between the source and dest target orientations and added to the final cost of considering the particular grasp/goal pair. 0 if doesn't matter. By default it is 0 so not to penalize the orientations"),
            "type": "number",
            "default":0,
            "tags":["si", "motion", "system", "advanced"]
        },
        "steplength": {
            "title": _("Steplength"),
            "description": _("rad, The minimum step size when exploring the space when planning with P2P movements"),
            "type": "number",
            "default":0.02,
            "tags":["si", "motion", "advanced"]
        },
        "targetdestikthresh": {
            "title": _("Targetdestikthresh"),
            "description": _("how much to prioritize top most objects in the container. The higher the value, the more will be prioritized."),
            "type": "number",
            "default": 0.01,
            "tags":["si", "motion", "target", "advanced"]
        },
        "targetenvclearance": {
            "title": _("Environment clearance near target"),
            "description": _("mm, how much to clear pointcloud near the detected target"),
            "type": "number",
            "default": 20,
            "tags":["si", "target", "basic", "system"]
        },
        "targetGraspTimeLimit":{
            "title": _("Target grasp time limit"),
            "description": _("sec, max time to spend on computing grasps for one target. 0 means infinite"),
            "type": "number",
            "default": 0,
            "tags":["motion", "medium", "si", "target"]
        },
        "targetIsRandomBox": {
            "title": _("Is target is a random box"),
            "description": _("if True, then using randomized box picking which means vision will send results with the box sizes in it"),
            "type": "boolean",
            "tags":["advanced", "si", "target", "system"]
        },
        "targetnamepattern": {
            "title": _("Name pattern of the target"),
            "description": _("supports regular expressions (i.e. detected_\\d+)"),
            "type": "string",
            "tags":["si", "advanced", "target"]
        },
        "targetPriorityForAngleMult": {
            "title": _("TargetPriorityForAngleMult"),
            "description": _("how much to prioritize oriented objects in the container depending on angle of Z axis to gravity. The higher the value, the more will be prioritized."),
            "type": "number",
            "tags":["advanced", "motion", "target", "si"]
        },
        "targetPriorityForXYCenterDist": {
            "title": _("TargetPriorityForXYCenterDist"),
            "description": _("how much to prioritize objects based on distance from center of container."),
            "type": "number",
            "default": 1.0,
            "tags":["advanced", "motion", "target", "si"]
        },        
        "targetPriorityForZMult": {
            "title": _("TargetPriorityForZMult"),
            "description": _("how much to prioritize top most objects in the container. The higher the value, the more will be prioritized."),
            "type": "number",
            "default": 10.0,
            "tags":["advanced", "motion", "target", "si"]
        },
        "targeturi":{
            "title": _("Target URI"),
            "description": _("optional URI to use for every target. if randomized box picking, then leave empty"),
            "type": "string",
            "default": "",
            "tags":["advanced", "dev", "target"]
        },
        "toolSpeedAccelOptions": { 
            "title": _("Tool speed and acceleration options"),
            "description": _("if 1 is set, then use fMaxManipSpeed/fMaxManipAccel for transferring when robot is grasping target. If 2 is set, then use for any other point to point movements. By default it is 0 (no constraint)"),
            "type": "integer",
            "minimum": 0,
            "maximum": 2,
            "default": 0,
            "tags":["motion", "basic", "si", "transfer"]
        },        
        "torqueDistThresh": { 
            "title": _("Torque distance threshold"),
            "description": _("mm, when gravity compensation is enabled, how many mm offset the robot could get from its commanded position before declaring a torque limits error"),
            "type": "number",
            "minimum": 0,
            "default": 15,
            "tags":["motion", "si", "medium"]
        },
        "useExecutionQueueing": {
            "title": _("Use execution queueing mode"),
            "description": _("to use queueing to speed up robot execution, 0 to not use queueing (use for debugging since it is simpler)"),
            "type": "integer",
            "default":1,
            "enum": [0,1],
            "tags":["dev", "advanced", "system"]
        },
        "useworkspaceplanner": {
            "title": _("Use workspace planner"),
            "description": _("If 1 is set, will try the workspace planner for moving the hand straight. If 2 is set, will try the RRT for moving straight. If 4 will fallback on workspace optimizer if greedy workspace tracker doesn't work. Can set 7 for trying all."),
            "type": "integer",
            "default":1,
            "tags":["motion", "advanced", "si"]
        },
        "verifyExecutionDynamicPointCloud": {
            "title": _("Verify execution dynamic point cloud"),
            "description": _("if 0 then do no verification once robot is executing trajectory, when 1 perform verification of the latest scene, when 2 perform verification with point clouds that have been added with the executionverification flag."),
            "type": "integer",
            "default":2,
            "enum": [0,1,2],
            "tags":["si", "system", "medium"]
        },
        "waitForSupplyTimeout":{
            "title": _("Wait for supply timeout"),
            "description": _("sec, how long to wait before stopping the pick and place thread when container is not empty, but nothing is registered. possibly change this depending on the detection recognition time"),
            "type": "number",
            "default": 30.0,
            "tags":["medium", "si", "system"]
        },
        "waitUpdateStampTimeout":{
            "title": _("Wait for update stamp timeout"),
            "description": _("sec, how long to wait for the initial vision results to come before starting pick and place"),
            "type": "number",
            "default": 30.0,
            "tags":["medium", "si", "system"]
        },        
        "worksteplength": {
            "title": _("Linear work step"),
            "description": _("m, When doing linear approach and depart, sample the workspace by this amount and then have the robot go through it. The larger the value, the less linear the tool moves, but it succeeds more often and computes faster."),
            "type": "number",
            "minimum": 0,
            "default": 0.01,
            "tags":["motion", "advanced", "si"]
        },
    },
}
