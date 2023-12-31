from core_data_modules.cleaners import Codes, somali
from dateutil.parser import isoparse
from src.pipeline_configuration_spec import *


PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="WorldBank-CPF-S01",
    test_participant_uuids=[
        "avf-participant-uuid-368c7741-7034-474a-9a87-6ae32a51f5a0",
        "avf-participant-uuid-5ca68e07-3dba-484b-a29c-7a6c989036b7",
        "avf-participant-uuid-45d15c2d-623c-4f89-bd91-7518147bf1dc",
        "avf-participant-uuid-88ef05ba-4c56-41f8-a00c-29104abab73e",
        "avf-participant-uuid-d9745740-3da5-43cc-a9d1-37fccb75380b",
        "avf-participant-uuid-96ff0ba1-a7df-4715-84c5-9c90e9093eb4"
    ],
    engagement_database=EngagementDatabaseClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-engagement-databases-firebase-credentials-file.json",
        database_path="engagement_databases/WorldBank-CPF"
    ),
    uuid_table=UUIDTableClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-id-infrastructure-firebase-adminsdk-6xps8-b9173f2bfd.json",
        table_name="avf-global-urn-to-participant-uuid",
        uuid_prefix="avf-participant-uuid-"
    ),
    operations_dashboard=OperationsDashboardConfiguration(
        credentials_file_url="gs://avf-credentials/avf-dashboards-firebase-adminsdk-gvecb-ef772e79b6.json"
    ),
    rapid_pro_sources=[
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/worldbank-cpf-text-it-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("worldbank_cpf_s01_demog", "worldbank_district", "location"),
                    FlowResultConfiguration("worldbank_cpf_s01_demog", "worldbank_gender", "gender"),
                    FlowResultConfiguration("worldbank_cpf_s01_demog", "worldbank_age", "age"),
                    FlowResultConfiguration("worldbank_cpf_s01_demog", "worldbank_currently_displaced", "currently_displaced"),
                    FlowResultConfiguration("worldbank_cpf_s01_demog", "worldbank_disability", "disability"),
                    FlowResultConfiguration("worldbank_cpf_s01_demog", "worldbank_household_language", "household_language"),

                    FlowResultConfiguration("wb_cpf_s01_sdc_pdrc_invitation", "worldbank_invitation_2023", "worldbank_cpf_s01_invitation"),
                    FlowResultConfiguration("wb_cpf_s01_wb_s01_invitation", "worldbank_invitation_2023", "worldbank_cpf_s01_invitation"),

                    # This project was originally called WorldBank-SCD s02, which is why this flow maps from
                    # scd_s02e01 to cpf_s01e01
                    FlowResultConfiguration("worldbank_cpf_s01e01_activation", "rqa_worldbank_scd_s02e01", "worldbank_cpf_s01e01"),
                    FlowResultConfiguration("worldbank_cpf_s01e02_activation", "rqa_worldbank_cpf_s01e02", "worldbank_cpf_s01e02"),
                    FlowResultConfiguration("worldbank_cpf_s01e03_activation", "rqa_worldbank_cpf_s01e03", "worldbank_cpf_s01e03"),
                    FlowResultConfiguration("worldbank_cpf_s01e04_activation", "rqa_worldbank_cpf_s01e04", "worldbank_cpf_s01e04"),
                    FlowResultConfiguration("worldbank_cpf_s01e04_activation", "rqa_worldbank_cpf_s01e04", "worldbank_cpf_s01e04"),

                    # The s01e01 question was re-asked at the end of the project to compensate for low-numbers in the
                    # first week, caused in part by short code issues.
                    # Include the re-asked question in the main s01e01 dataset.
                    FlowResultConfiguration("worldbank_cpf_s01e01_repeat_activation", "rqa_worldbank_cpf_s01e01_repeat", "worldbank_cpf_s01e01"),

                    # The s01e04 show was repeated at the end of the project due difficulties finding a guest
                    # the first time the show was broadcast.
                    FlowResultConfiguration("worldbank_cpf_s01e04_repeat_activation", "rqa_worldbank_cpf_s01e04_repeat", "worldbank_cpf_s01e04"),

                    FlowResultConfiguration("worldbank_cpf_s01_close_out_activation", "rqa_worldbank_cpf_s01_close_out", "worldbank_cpf_s01_closeout"),
                ]
            )
        )
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations=[
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_s01_invitation",
                    engagement_db_dataset="worldbank_cpf_s01_invitation",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/s01_invitation"),
                                                coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="worldbank_cpf_s01_invitation"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_s01e01",
                    engagement_db_dataset="worldbank_cpf_s01e01",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/s01e01"),
                                                coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="worldbank_cpf_s01e01"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_s01e02",
                    engagement_db_dataset="worldbank_cpf_s01e02",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/s01e02"),
                                                coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="worldbank_cpf_s01e02"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_s01e03",
                    engagement_db_dataset="worldbank_cpf_s01e03",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/s01e03"),
                                                coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="worldbank_cpf_s01e03"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_s01e04",
                    engagement_db_dataset="worldbank_cpf_s01e04",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/s01e04"),
                                                coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="worldbank_cpf_s01e04"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_s01_closeout",
                    engagement_db_dataset="worldbank_cpf_s01_closeout",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/s01_closeout"),
                                                coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="worldbank_cpf_s01_closeout"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_age",
                    engagement_db_dataset="age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/age"),
                                                auto_coder=lambda text: str(
                                                    somali.DemographicCleaner.clean_age_within_range(text))
                                                ),
                    ],
                    ws_code_match_value="age"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_gender",
                    engagement_db_dataset="gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/gender"),
                                                auto_coder=somali.DemographicCleaner.clean_gender)
                    ],
                    ws_code_match_value="gender"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_household_language",
                    engagement_db_dataset="household_language",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/household_language"), auto_coder=None)
                    ],
                    ws_code_match_value="household_language"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_location",
                    engagement_db_dataset="location",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/mogadishu_sub_district"),
                                                auto_coder=somali.DemographicCleaner.clean_mogadishu_sub_district),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/somalia_district"), auto_coder=lambda text:
                                                somali.DemographicCleaner.clean_somalia_district(text)
                                                if somali.DemographicCleaner.clean_mogadishu_sub_district == Codes.NOT_CODED else Codes.NOT_CODED),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/somalia_region"), auto_coder=None),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/somalia_state"), auto_coder=None),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/somalia_zone"), auto_coder=None),
                    ],
                    ws_code_match_value="location"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_currently_displaced",
                    engagement_db_dataset="currently_displaced",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/currently_displaced"),
                                                auto_coder=somali.DemographicCleaner.clean_yes_no)
                    ],
                    ws_code_match_value="currently_displaced"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WorldBank_CPF_disability",
                    engagement_db_dataset="disability",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/disability"),
                                                auto_coder=somali.DemographicCleaner.clean_yes_no)
                    ],
                    ws_code_match_value="disability"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2023/WorldBank-CPF/coda_users.json"
        )
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2023/WorldBank-CPF-S01"
    ),
    analysis=AnalysisConfiguration(
        google_drive_upload=GoogleDriveUploadConfiguration(
            credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json",
            drive_dir="worldbank_cpf_analysis_outputs/s01"
        ),
        dataset_configurations=[
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["worldbank_cpf_s01e01"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="s01e01_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/s01e01"),
                        analysis_dataset="s01e01"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["worldbank_cpf_s01e02"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="s01e02_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/s01e02"),
                        analysis_dataset="s01e02"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["worldbank_cpf_s01e03"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="s01e03_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/s01e03"),
                        analysis_dataset="s01e03"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["worldbank_cpf_s01e04"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="s01e04_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/s01e04"),
                        analysis_dataset="s01e04"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["worldbank_cpf_s01_closeout"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="s01_closeout_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/s01_closeout"),
                        analysis_dataset="s01_closeout"
                    )
                ]
            ),
            OperatorDatasetConfiguration(
                raw_dataset="operator_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/operator"),
                        analysis_dataset="operator",
                        analysis_location=AnalysisLocations.SOMALIA_OPERATOR
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["age"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="age_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/age"),
                        analysis_dataset="age"
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/age_category"),
                        analysis_dataset="age_category",
                        age_category_config=AgeCategoryConfiguration(
                            age_analysis_dataset="age",
                            categories={
                                (10, 14): "10 to 14",
                                (15, 17): "15 to 17",
                                (18, 35): "18 to 35",
                                (36, 54): "36 to 54",
                                (55, 99): "55 to 99"
                            }
                        )
                    ),
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["gender"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="gender_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/gender"),
                        analysis_dataset="gender"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["location"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="location_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/mogadishu_sub_district"),
                        analysis_dataset="mogadishu_sub_district",
                        analysis_location=AnalysisLocations.MOGADISHU_SUB_DISTRICT
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/somalia_district"),
                        analysis_dataset="district",
                        analysis_location=AnalysisLocations.SOMALIA_DISTRICT
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/somalia_region"),
                        analysis_dataset="region",
                        analysis_location=AnalysisLocations.SOMALIA_REGION
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/somalia_state"),
                        analysis_dataset="state",
                        analysis_location=AnalysisLocations.SOMALIA_STATE
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/somalia_zone"),
                        analysis_dataset="zone",
                        analysis_location=AnalysisLocations.SOMALIA_ZONE
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["currently_displaced"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="currently_displaced",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/currently_displaced"),
                        analysis_dataset="currently_displaced"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["household_language"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="household_language",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/household_language"),
                        analysis_dataset="household_language"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["disability"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="disability",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/disability"),
                        analysis_dataset="disability"
                    )
                ]
            ),
        ],
        ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset")
    )
)
