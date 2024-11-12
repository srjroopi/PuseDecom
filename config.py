# config.py
ENVIRONMENT = "qa"  # type: ignore # prod/stg/qa

QA_CONSTANTS = {
    'TOKEN_URL'                 :   'https://login-stg.pearson.com/v1/piapi-int/login/webcredentials',
    'PRISM_TOC_API'             :   'https://prism-qa.pearsoned.com/api/contenttoc/v1/assets?',
    'PRISM_PAGE_MAPPING_API'    :   'https://prism-qa.pearsoned.com/api/contenttoc/v1/assets/page-mapping',
    'CSG_PRODUCT_API'           :   'https://content-service-qa.stg-prsn.com/csg/api/v3/search',
    'COURSE_API'                :   'https://stpaperapiqa.stg-prsn.com/etext/v2/courseboot/book/coursebookcatalogue',
    'RESOURCE_API'              :   'https://prism-qa.pearsoned.com/api/contenttoc/v1/assets/hotspot?',

    #PAPER API Specific
    'TIBRON_USERNAME'   : "tiburon_system",
    'TIBRON_PASSWORD'   : "pqGgHrjfetxH7rMKJuEqCJF3SPAE8CEQ",
}