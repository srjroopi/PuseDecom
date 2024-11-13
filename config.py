# config.py
ENVIRONMENT = "qa"  # type: ignore # prod/stg/qa

QA_CONSTANTS = {
    # 'TOKEN_URL'                 :   'https://piapi-internal.openclass.com/tokens',
    'TOKEN_URL'                 :   'https://int-piapi-internal.stg-openclass.com/tokens/',
    'PRISM_TOC_API'             :   'https://prism-qa.pearsoned.com/api/contenttoc/v1/assets?',
    'PRISM_PAGE_MAPPING_API'    :   'https://prism-qa.pearsoned.com/api/contenttoc/v1/assets/page-mapping',
    'CSG_TOKEN'                 :   'https://tst-piapi-internal.dev-openclass.com/tokens',
    'CSG_PRODUCT_API'           :   'https://content-service-qa.stg-prsn.com/csg/api/v3/search',
    'COURSE_API'                :   'https://stpaperapiqa.stg-prsn.com/etext/v2/courseboot/book/coursebookcatalogue',
    'RESOURCE_API'              :   'https://prism-qa.pearsoned.com/api/contenttoc/v1/assets/hotspot?',

    #PAPER API Specific
    'CSG_TOKEN_USERNAME'   :    "evergreen_system",
    'CSG_TOKEN_PASSWORD'   :    "HjwQIr1KWol2lZ9K92IIpSX47QPjGQHe",

    #systosys Login
    'SYS_TOKEN_USERNAME'    :   "ereader_platform_system",
    'SYS_TOKEN_PASSWORD'    :   "sNOFvGz6maQPApjxD1b5awSePzwC0YGj"
}