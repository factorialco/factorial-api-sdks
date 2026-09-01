from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesPayrollEmployeesGermanEmployeeDataBody")


@_attrs_define
class PostApi20261001ResourcesPayrollEmployeesGermanEmployeeDataBody:
    employee_id: str
    """ Identifier of the employee """
    work_permit_expiration_date: str | Unset = UNSET
    """ Expiration date of the employee's work permit """
    residency_permit_expiration_date: str | Unset = UNSET
    """ Expiration date of the employee's residence permit """
    certificate_of_study_expiration_date: str | Unset = UNSET
    """ Expiration date of the employee's certificate of study """
    health_insurer_company_number: str | Unset = UNSET
    """ Company number of the employee's health insurance company """
    contribution_class_health_insurance: int | Unset = UNSET
    """ Health insurance contribution class. 0: No contribution (private health insurance or voluntary health
    insurance as self-payer), 1: General contribution, 3: Reduced contribution, 4: Contribution to agricultural
    health insurance, 5: Employer's contribution to agricultural health insurance, 6: Flat-rate contribution for
    marginal employees, 9: Corporate payer """
    contribution_class_unemployment_insurance: int | Unset = UNSET
    """ Unemployment insurance contribution class. 0: No contribution, 1: Full contribution, 2: Half contribution
    """
    contribution_class_pension_insurance: int | Unset = UNSET
    """ Pension insurance contribution class. 0: No contribution, 1: Full contribution, 3: Half contribution, 5:
    Flat-rate contribution for marginal employees """
    contribution_class_nursing_insurance: int | Unset = UNSET
    """ Long-term (nursing) insurance contribution class. 0: No contribution, 1: Full contribution, 2: Half
    contribution """
    additional_contribution_to_nursing_insurance: bool | Unset = UNSET
    """ Whether the employee pays an additional contribution to the nursing insurance institution """
    tax_class: int | Unset = UNSET
    """ Tax class of the employee """
    requested_annual_allowance: int | Unset = UNSET
    """ Requested annual tax allowance """
    factor: float | Unset = UNSET
    """ Factor used for the factor method (Faktorverfahren) in German income tax """
    annual_tax_allowance: int | Unset = UNSET
    """ Annual tax allowance """
    monthly_tax_allowance: int | Unset = UNSET
    """ Monthly tax allowance """
    child_tax_allowance: float | Unset = UNSET
    """ Child tax allowance """
    denomination: str | Unset = UNSET
    """ Denomination of the employee. ev: Protestant Church Tax, rk: Roman Catholic Church Tax, ak: Old Catholic
    Church Tax, fa: Free Religious Community Alzey, fb: Free Religious State Community Baden, fg: Free Religious
    State Community Palatinate, fm: Free Religious Community Mainz, fr: French Reformed (until 12/2015), fs: Free
    Religious Community Offenbach/Main, ib: Israelite Religious Community Baden, ih: Jewish Cult Tax, il: Israelite
    Cult Tax of Cult-Entitled Communities, is: Israelite / Jewish Cult Tax, iw: Israelite Religious Community
    Württemberg, jd: Jewish Cult Tax, jh: Jewish Cult Tax, lt: Evangelical Lutheran (until 12/2015), rf: Evangelical
    Reformed (until 12/2015), nd: Non-denominational """
    spouses_denomination: str | Unset = UNSET
    """ Denomination of the employee's spouse. ev: Protestant Church Tax, rk: Roman Catholic Church Tax, ak: Old
    Catholic Church Tax, fa: Free Religious Community Alzey, fb: Free Religious State Community Baden, fg: Free
    Religious State Community Palatinate, fm: Free Religious Community Mainz, fr: French Reformed (until 12/2015),
    fs: Free Religious Community Offenbach/Main, ib: Israelite Religious Community Baden, ih: Jewish Cult Tax, il:
    Israelite Cult Tax of Cult-Entitled Communities, is: Israelite / Jewish Cult Tax, iw: Israelite Religious
    Community Württemberg, jd: Jewish Cult Tax, jh: Jewish Cult Tax, lt: Evangelical Lutheran (until 12/2015), rf:
    Evangelical Reformed (until 12/2015), nd: Non-denominational """
    personnel_leasing: int | Unset = UNSET
    """ Personnel leasing status of the employee. 0: such as client data, 1: no, 2: yes """
    highest_level_of_professional_training: int | Unset = UNSET
    """ Highest level of professional training of the employee. 0: No specification, 1: Without vocational
    qualification, 2: Completion of recognized vocational training, 3: Master craftsman/technician or equivalent
    technical school degree, 4: Bachelor, 5: Diploma/Magister/Master/State examination, 6: Doctorate, 9:
    Qualification unknown """
    highest_level_of_education: int | Unset = UNSET
    """ Highest level of education of the employee. 0: No specification, 1: Without school qualification, 2:
    Secondary school diploma, 3: Intermediate school diploma or equivalent, 4: High school diploma/vocational
    diploma, 9: Qualification unknown """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        work_permit_expiration_date = self.work_permit_expiration_date

        residency_permit_expiration_date = self.residency_permit_expiration_date

        certificate_of_study_expiration_date = self.certificate_of_study_expiration_date

        health_insurer_company_number = self.health_insurer_company_number

        contribution_class_health_insurance = self.contribution_class_health_insurance

        contribution_class_unemployment_insurance = self.contribution_class_unemployment_insurance

        contribution_class_pension_insurance = self.contribution_class_pension_insurance

        contribution_class_nursing_insurance = self.contribution_class_nursing_insurance

        additional_contribution_to_nursing_insurance = (
            self.additional_contribution_to_nursing_insurance
        )

        tax_class = self.tax_class

        requested_annual_allowance = self.requested_annual_allowance

        factor = self.factor

        annual_tax_allowance = self.annual_tax_allowance

        monthly_tax_allowance = self.monthly_tax_allowance

        child_tax_allowance = self.child_tax_allowance

        denomination = self.denomination

        spouses_denomination = self.spouses_denomination

        personnel_leasing = self.personnel_leasing

        highest_level_of_professional_training = self.highest_level_of_professional_training

        highest_level_of_education = self.highest_level_of_education

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
            }
        )
        if work_permit_expiration_date is not UNSET:
            field_dict["work_permit_expiration_date"] = work_permit_expiration_date
        if residency_permit_expiration_date is not UNSET:
            field_dict["residency_permit_expiration_date"] = residency_permit_expiration_date
        if certificate_of_study_expiration_date is not UNSET:
            field_dict["certificate_of_study_expiration_date"] = (
                certificate_of_study_expiration_date
            )
        if health_insurer_company_number is not UNSET:
            field_dict["health_insurer_company_number"] = health_insurer_company_number
        if contribution_class_health_insurance is not UNSET:
            field_dict["contribution_class_health_insurance"] = contribution_class_health_insurance
        if contribution_class_unemployment_insurance is not UNSET:
            field_dict["contribution_class_unemployment_insurance"] = (
                contribution_class_unemployment_insurance
            )
        if contribution_class_pension_insurance is not UNSET:
            field_dict["contribution_class_pension_insurance"] = (
                contribution_class_pension_insurance
            )
        if contribution_class_nursing_insurance is not UNSET:
            field_dict["contribution_class_nursing_insurance"] = (
                contribution_class_nursing_insurance
            )
        if additional_contribution_to_nursing_insurance is not UNSET:
            field_dict["additional_contribution_to_nursing_insurance"] = (
                additional_contribution_to_nursing_insurance
            )
        if tax_class is not UNSET:
            field_dict["tax_class"] = tax_class
        if requested_annual_allowance is not UNSET:
            field_dict["requested_annual_allowance"] = requested_annual_allowance
        if factor is not UNSET:
            field_dict["factor"] = factor
        if annual_tax_allowance is not UNSET:
            field_dict["annual_tax_allowance"] = annual_tax_allowance
        if monthly_tax_allowance is not UNSET:
            field_dict["monthly_tax_allowance"] = monthly_tax_allowance
        if child_tax_allowance is not UNSET:
            field_dict["child_tax_allowance"] = child_tax_allowance
        if denomination is not UNSET:
            field_dict["denomination"] = denomination
        if spouses_denomination is not UNSET:
            field_dict["spouses_denomination"] = spouses_denomination
        if personnel_leasing is not UNSET:
            field_dict["personnel_leasing"] = personnel_leasing
        if highest_level_of_professional_training is not UNSET:
            field_dict["highest_level_of_professional_training"] = (
                highest_level_of_professional_training
            )
        if highest_level_of_education is not UNSET:
            field_dict["highest_level_of_education"] = highest_level_of_education

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        work_permit_expiration_date = d.pop("work_permit_expiration_date", UNSET)

        residency_permit_expiration_date = d.pop("residency_permit_expiration_date", UNSET)

        certificate_of_study_expiration_date = d.pop("certificate_of_study_expiration_date", UNSET)

        health_insurer_company_number = d.pop("health_insurer_company_number", UNSET)

        contribution_class_health_insurance = d.pop("contribution_class_health_insurance", UNSET)

        contribution_class_unemployment_insurance = d.pop(
            "contribution_class_unemployment_insurance", UNSET
        )

        contribution_class_pension_insurance = d.pop("contribution_class_pension_insurance", UNSET)

        contribution_class_nursing_insurance = d.pop("contribution_class_nursing_insurance", UNSET)

        additional_contribution_to_nursing_insurance = d.pop(
            "additional_contribution_to_nursing_insurance", UNSET
        )

        tax_class = d.pop("tax_class", UNSET)

        requested_annual_allowance = d.pop("requested_annual_allowance", UNSET)

        factor = d.pop("factor", UNSET)

        annual_tax_allowance = d.pop("annual_tax_allowance", UNSET)

        monthly_tax_allowance = d.pop("monthly_tax_allowance", UNSET)

        child_tax_allowance = d.pop("child_tax_allowance", UNSET)

        denomination = d.pop("denomination", UNSET)

        spouses_denomination = d.pop("spouses_denomination", UNSET)

        personnel_leasing = d.pop("personnel_leasing", UNSET)

        highest_level_of_professional_training = d.pop(
            "highest_level_of_professional_training", UNSET
        )

        highest_level_of_education = d.pop("highest_level_of_education", UNSET)

        post_api_20261001_resources_payroll_employees_german_employee_data_body = cls(
            employee_id=employee_id,
            work_permit_expiration_date=work_permit_expiration_date,
            residency_permit_expiration_date=residency_permit_expiration_date,
            certificate_of_study_expiration_date=certificate_of_study_expiration_date,
            health_insurer_company_number=health_insurer_company_number,
            contribution_class_health_insurance=contribution_class_health_insurance,
            contribution_class_unemployment_insurance=contribution_class_unemployment_insurance,
            contribution_class_pension_insurance=contribution_class_pension_insurance,
            contribution_class_nursing_insurance=contribution_class_nursing_insurance,
            additional_contribution_to_nursing_insurance=additional_contribution_to_nursing_insurance,
            tax_class=tax_class,
            requested_annual_allowance=requested_annual_allowance,
            factor=factor,
            annual_tax_allowance=annual_tax_allowance,
            monthly_tax_allowance=monthly_tax_allowance,
            child_tax_allowance=child_tax_allowance,
            denomination=denomination,
            spouses_denomination=spouses_denomination,
            personnel_leasing=personnel_leasing,
            highest_level_of_professional_training=highest_level_of_professional_training,
            highest_level_of_education=highest_level_of_education,
        )

        post_api_20261001_resources_payroll_employees_german_employee_data_body.additional_properties = d
        return post_api_20261001_resources_payroll_employees_german_employee_data_body

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
