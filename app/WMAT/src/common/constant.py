
class Field(object):
    #charset
    CHARSET_UTF8='utf-8'

    # yaml field  1. key name
    # Page Steps
    ELEMENT = 'element'
    ACTION = 'action'
    EXPECTATION = 'expectation'
    PAGE = 'page'
    DATA = 'data'
    STEP_DESC = 'step_desc'
    VALUE = 'value'
    TYPE = 'type'
    IOS_NAME='ios_name'
    # Scenarios
    SCENARIOS_NAME = 'scenarios_name'
    PAGE_STEPS = 'page_steps'
    # test case
    TESTCASE_NAME = 'testcase_name'
    SCENARIOS_SUITES = 'scenarios_suites'
    PACKAGE_NAME='package_name'
    SET_UP='setUp'
    TEAR_DOWN='tearDown'

    # yaml field  2. action type
    ACTION_TYPE='type'
    ACTION_CLICK='click'
    ACTION_TYPEENTER='typeEnter'
    ACTION_TAP='tap'
    ACTION_SWIPE='swipe'
    ACTION_FLICK='flick'
    ACTION_WAIT='wait'
    ACTION_SWITCH_TO_NATIVE='switch_to_native'
    ACTION_SWITCH_TO_WEBVIEW='switch_to_webview'
    ACTION_SWITCH_TO_APP='switch_to_app'
    ACTION_BACKGROUND_APP='background_app'
    ACTION_CURRENT_ACTIVITY='get_current_activity'
    ACTION_TYPE_EXT='type_ext'

    # yaml field  2. expectation matching type
    EXPECTATION_MATCHING_TYPE="matching"
    EXPECTATION_ATTR='attr'
    EXPECTATION_REGEX_TYPE="regex"
    EXPECTATION_TYPE_TOAST = 'toast'
    EXPECTATION_MATCHING_TYPE_CONTAINS = 'contains'
    EXPECTATION_MATCHING_TYPE_NOT_EQUALS = 'notEquals'
    EXPECTATION_MATCHING_TYPE_NOT_CONTAINS = 'notContains'

    #device yaml conf
    ACTIVE='active'
    DEVICES='devices'
    APP='app'
    URL='url'
    PLATFROM_NAME='platformName'
    DEVICE_NAME='deviceName'
    PLATFORM_VERSION='platformVersion'
    APP_PACKAGE='appPackage'
    APP_ACTIVITY='appActivity'
    DRIVER_AUTOMATIONNAME='automationName'

class CONFIG(object):

    # toast temp screenshot file folder and names
    TEMP_PIC_DIR = "../../temp/"

class GlobalVar:
    YAML_PATH=''
