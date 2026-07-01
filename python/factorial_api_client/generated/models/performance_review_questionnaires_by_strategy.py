from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_review_questionnaires_by_strategy_direct_report_questionnaire import (
        PerformanceReviewQuestionnairesByStrategyDirectReportQuestionnaire,
    )
    from ..models.performance_review_questionnaires_by_strategy_employee_potential_score_manager_questionnaire import (
        PerformanceReviewQuestionnairesByStrategyEmployeePotentialScoreManagerQuestionnaire,
    )
    from ..models.performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire import (
        PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaire,
    )
    from ..models.performance_review_questionnaires_by_strategy_employee_score_self_questionnaire import (
        PerformanceReviewQuestionnairesByStrategyEmployeeScoreSelfQuestionnaire,
    )
    from ..models.performance_review_questionnaires_by_strategy_manager_questionnaire import (
        PerformanceReviewQuestionnairesByStrategyManagerQuestionnaire,
    )
    from ..models.performance_review_questionnaires_by_strategy_peers_questionnaire import (
        PerformanceReviewQuestionnairesByStrategyPeersQuestionnaire,
    )
    from ..models.performance_review_questionnaires_by_strategy_self_questionnaire import (
        PerformanceReviewQuestionnairesByStrategySelfQuestionnaire,
    )


T = TypeVar("T", bound="PerformanceReviewQuestionnairesByStrategy")


@_attrs_define
class PerformanceReviewQuestionnairesByStrategy:
    id: str
    """ Review process ID """
    performance_review_process_id: str
    """ Review process ID """
    default_rating_scale: list[Any]
    """ Scoring range used in rating questions """
    self_questionnaire: PerformanceReviewQuestionnairesByStrategySelfQuestionnaire | Unset = UNSET
    """ Questionnaire for self evaluation """
    manager_questionnaire: PerformanceReviewQuestionnairesByStrategyManagerQuestionnaire | Unset = (
        UNSET
    )
    """ Questionnaire for manager evaluation """
    direct_report_questionnaire: (
        PerformanceReviewQuestionnairesByStrategyDirectReportQuestionnaire | Unset
    ) = UNSET
    """ Questionnaire for direct report evaluation """
    peers_questionnaire: PerformanceReviewQuestionnairesByStrategyPeersQuestionnaire | Unset = UNSET
    """ Questionnaire for peers evaluation """
    employee_score_self_questionnaire: (
        PerformanceReviewQuestionnairesByStrategyEmployeeScoreSelfQuestionnaire | Unset
    ) = UNSET
    """ Questionnaire included in the end of self evaluation to evaluate the employee performance """
    employee_score_manager_questionnaire: (
        PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaire | Unset
    ) = UNSET
    """ Questionnaire included in the end of manager evaluation to evaluate the employee performance """
    employee_potential_score_manager_questionnaire: (
        PerformanceReviewQuestionnairesByStrategyEmployeePotentialScoreManagerQuestionnaire | Unset
    ) = UNSET
    """ Questionnaire included in the end of manager evaluation to evaluate the employee potential """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        performance_review_process_id = self.performance_review_process_id

        default_rating_scale = self.default_rating_scale

        self_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_questionnaire, Unset):
            self_questionnaire = self.self_questionnaire.to_dict()

        manager_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manager_questionnaire, Unset):
            manager_questionnaire = self.manager_questionnaire.to_dict()

        direct_report_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direct_report_questionnaire, Unset):
            direct_report_questionnaire = self.direct_report_questionnaire.to_dict()

        peers_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.peers_questionnaire, Unset):
            peers_questionnaire = self.peers_questionnaire.to_dict()

        employee_score_self_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.employee_score_self_questionnaire, Unset):
            employee_score_self_questionnaire = self.employee_score_self_questionnaire.to_dict()

        employee_score_manager_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.employee_score_manager_questionnaire, Unset):
            employee_score_manager_questionnaire = (
                self.employee_score_manager_questionnaire.to_dict()
            )

        employee_potential_score_manager_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.employee_potential_score_manager_questionnaire, Unset):
            employee_potential_score_manager_questionnaire = (
                self.employee_potential_score_manager_questionnaire.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "performance_review_process_id": performance_review_process_id,
                "default_rating_scale": default_rating_scale,
            }
        )
        if self_questionnaire is not UNSET:
            field_dict["self_questionnaire"] = self_questionnaire
        if manager_questionnaire is not UNSET:
            field_dict["manager_questionnaire"] = manager_questionnaire
        if direct_report_questionnaire is not UNSET:
            field_dict["direct_report_questionnaire"] = direct_report_questionnaire
        if peers_questionnaire is not UNSET:
            field_dict["peers_questionnaire"] = peers_questionnaire
        if employee_score_self_questionnaire is not UNSET:
            field_dict["employee_score_self_questionnaire"] = employee_score_self_questionnaire
        if employee_score_manager_questionnaire is not UNSET:
            field_dict["employee_score_manager_questionnaire"] = (
                employee_score_manager_questionnaire
            )
        if employee_potential_score_manager_questionnaire is not UNSET:
            field_dict["employee_potential_score_manager_questionnaire"] = (
                employee_potential_score_manager_questionnaire
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_questionnaires_by_strategy_direct_report_questionnaire import (
            PerformanceReviewQuestionnairesByStrategyDirectReportQuestionnaire,
        )
        from ..models.performance_review_questionnaires_by_strategy_employee_potential_score_manager_questionnaire import (
            PerformanceReviewQuestionnairesByStrategyEmployeePotentialScoreManagerQuestionnaire,
        )
        from ..models.performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire import (
            PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaire,
        )
        from ..models.performance_review_questionnaires_by_strategy_employee_score_self_questionnaire import (
            PerformanceReviewQuestionnairesByStrategyEmployeeScoreSelfQuestionnaire,
        )
        from ..models.performance_review_questionnaires_by_strategy_manager_questionnaire import (
            PerformanceReviewQuestionnairesByStrategyManagerQuestionnaire,
        )
        from ..models.performance_review_questionnaires_by_strategy_peers_questionnaire import (
            PerformanceReviewQuestionnairesByStrategyPeersQuestionnaire,
        )
        from ..models.performance_review_questionnaires_by_strategy_self_questionnaire import (
            PerformanceReviewQuestionnairesByStrategySelfQuestionnaire,
        )

        d = dict(src_dict)
        id = d.pop("id")

        performance_review_process_id = d.pop("performance_review_process_id")

        default_rating_scale = cast(list[Any], d.pop("default_rating_scale"))

        _self_questionnaire = d.pop("self_questionnaire", UNSET)
        self_questionnaire: PerformanceReviewQuestionnairesByStrategySelfQuestionnaire | Unset
        if isinstance(_self_questionnaire, Unset):
            self_questionnaire = UNSET
        else:
            self_questionnaire = (
                PerformanceReviewQuestionnairesByStrategySelfQuestionnaire.from_dict(
                    _self_questionnaire
                )
            )

        _manager_questionnaire = d.pop("manager_questionnaire", UNSET)
        manager_questionnaire: PerformanceReviewQuestionnairesByStrategyManagerQuestionnaire | Unset
        if isinstance(_manager_questionnaire, Unset):
            manager_questionnaire = UNSET
        else:
            manager_questionnaire = (
                PerformanceReviewQuestionnairesByStrategyManagerQuestionnaire.from_dict(
                    _manager_questionnaire
                )
            )

        _direct_report_questionnaire = d.pop("direct_report_questionnaire", UNSET)
        direct_report_questionnaire: (
            PerformanceReviewQuestionnairesByStrategyDirectReportQuestionnaire | Unset
        )
        if isinstance(_direct_report_questionnaire, Unset):
            direct_report_questionnaire = UNSET
        else:
            direct_report_questionnaire = (
                PerformanceReviewQuestionnairesByStrategyDirectReportQuestionnaire.from_dict(
                    _direct_report_questionnaire
                )
            )

        _peers_questionnaire = d.pop("peers_questionnaire", UNSET)
        peers_questionnaire: PerformanceReviewQuestionnairesByStrategyPeersQuestionnaire | Unset
        if isinstance(_peers_questionnaire, Unset):
            peers_questionnaire = UNSET
        else:
            peers_questionnaire = (
                PerformanceReviewQuestionnairesByStrategyPeersQuestionnaire.from_dict(
                    _peers_questionnaire
                )
            )

        _employee_score_self_questionnaire = d.pop("employee_score_self_questionnaire", UNSET)
        employee_score_self_questionnaire: (
            PerformanceReviewQuestionnairesByStrategyEmployeeScoreSelfQuestionnaire | Unset
        )
        if isinstance(_employee_score_self_questionnaire, Unset):
            employee_score_self_questionnaire = UNSET
        else:
            employee_score_self_questionnaire = (
                PerformanceReviewQuestionnairesByStrategyEmployeeScoreSelfQuestionnaire.from_dict(
                    _employee_score_self_questionnaire
                )
            )

        _employee_score_manager_questionnaire = d.pop("employee_score_manager_questionnaire", UNSET)
        employee_score_manager_questionnaire: (
            PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaire | Unset
        )
        if isinstance(_employee_score_manager_questionnaire, Unset):
            employee_score_manager_questionnaire = UNSET
        else:
            employee_score_manager_questionnaire = PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaire.from_dict(
                _employee_score_manager_questionnaire
            )

        _employee_potential_score_manager_questionnaire = d.pop(
            "employee_potential_score_manager_questionnaire", UNSET
        )
        employee_potential_score_manager_questionnaire: (
            PerformanceReviewQuestionnairesByStrategyEmployeePotentialScoreManagerQuestionnaire
            | Unset
        )
        if isinstance(_employee_potential_score_manager_questionnaire, Unset):
            employee_potential_score_manager_questionnaire = UNSET
        else:
            employee_potential_score_manager_questionnaire = PerformanceReviewQuestionnairesByStrategyEmployeePotentialScoreManagerQuestionnaire.from_dict(
                _employee_potential_score_manager_questionnaire
            )

        performance_review_questionnaires_by_strategy = cls(
            id=id,
            performance_review_process_id=performance_review_process_id,
            default_rating_scale=default_rating_scale,
            self_questionnaire=self_questionnaire,
            manager_questionnaire=manager_questionnaire,
            direct_report_questionnaire=direct_report_questionnaire,
            peers_questionnaire=peers_questionnaire,
            employee_score_self_questionnaire=employee_score_self_questionnaire,
            employee_score_manager_questionnaire=employee_score_manager_questionnaire,
            employee_potential_score_manager_questionnaire=employee_potential_score_manager_questionnaire,
        )

        performance_review_questionnaires_by_strategy.additional_properties = d
        return performance_review_questionnaires_by_strategy

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
