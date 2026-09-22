# MIHYE KANG

**Technical Program Management · Cloud Migration & AI Platform Delivery**

Seoul, South Korea · kangmihye@gmail.com · [LinkedIn](https://www.linkedin.com/in/%EB%AF%B8%ED%98%9C-%EA%B0%95-1a29ba2b9/)

---

## SUMMARY

17 years in enterprise IT at KT Group: 6 years in development and operations, 11 years leading technical programs as Program Manager and Project Lead. Specializes in engagements where no delivery standard exists yet: defines integration specifications, drives architecture decisions to closure across multi-vendor technical forums, and converts delivery status into tracked metrics rather than status narrative. Recent scope includes a 12-month, ~90-service Azure migration (on time, zero defects) and a three-party AI media agent integration program currently in delivery. CKA and AWS Solutions Architect Associate certified; authors Kubernetes manifests directly.

---

## PROGRAM DELIVERY HIGHLIGHTS

| Dimension | Evidence |
| --- | --- |
| Portfolio scale | ~90-service Azure migration program; 3 concurrent service lines managed simultaneously (2022–2023); 17 external partner organizations onboarded without reporting authority |
| Delivery outcome | 0 defects and on-time milestone completion with no added headcount (Azure, 2025); 99.8% manifest completion tracked to closure |
| Technical decision ownership | Non-HTTP (TCP/MQTT) integration architecture selected through a 5-option evaluation and adopted as the project-wide standard |
| Process innovation | Company-wide workload measurement process sustained for 6+ months after roll-off; fed the 2026 ITO rate revision |
| AI in delivery workflow | AI-assisted log analysis for root-cause narrowing; STT and LLM cascade pipeline design; Agentic AI certification program completed 2026.06 |

---

## PROFESSIONAL EXPERIENCE

### KTDS (KT Group IT subsidiary) · Program Manager / Project Lead · 2015.01 – Present

#### KT Azure Mass Migration · Non-ITO Project Lead · 2025.01 – 2025.12

**Context.** Company-wide migration of approximately 90 services to Azure. Owned the 6 non-standard Non-ITO services, for which the corporate migration guide provided no applicable criteria.

- **Requirements baseline.** Designed a 16-item structured discovery questionnaire covering current architecture, load profile (customer type, concurrent sessions), verification criteria (test scenarios, troubleshooting history), operating model (release cadence, CI/CD), data migration sizing, and security approval path. Applied uniformly across all 6 services to produce comparable inputs. Classified absent test scenarios as a missing success criterion rather than a documentation gap and required authoring before kickoff. Pre-cleared firewall requirements from the integration inventory, eliminating migration-day wait states.
- **Architecture decision.** The corporate guide assumed HTTP-only traffic, leaving no decision basis for the persistent TCP/MQTT integration in one of the 6 services. Led the technical forum across the architecture team, KT, KTC, and Microsoft. Evaluated 5 candidate architectures through a four-stage filter (technical feasibility, operational risk, change scope, environment fit) and selected AKS internal load balancer with pod-level TLS, rejecting public-preview App Gateway TCP/TLS and options requiring client or firmware rework. Adopted as the project-wide standard for non-HTTP traffic.
- **Delivery control.** Identified the absence of any means to track per-pod manifest progress as the problem itself. Designed a Confluence progress tracker operated as a management metric rather than a record, and tracked manifest completion to 99.8%.
- **Critical-path intervention.** When manifest authoring became the primary delay driver, learned the Kustomize manifest standard and authored manifests directly rather than waiting for headcount allocation. Obtained CKA during the program. Converted the architecture team's principles into a Kustomize manifest standard that partner vendors could apply without interpretation.
- **Incident analysis.** Narrowed Rancher logs to the failure window and used AI-assisted analysis to reduce the hypothesis space on a StatefulSet startup failure; confirmed and verified root cause as etcd state not reflecting a forced VM shutdown.
- **Knowledge retention.** Classified MariaDB-to-MySQL query conversion errors by type into a reusable reference for subsequent migration waves.

**Results.** All migration milestones delivered on time with no additional resources. Zero defects. All migrated services operating in production. TCP integration architecture adopted as project-wide standard.

**Stack.** Azure, AKS, Rancher, Kustomize, ArgoCD, Microsoft Entra ID, TCP/MQTT, MariaDB to MySQL, Jira, Confluence

#### KT ADD (AI Media Agent Integration) · Program Manager · 2026.05 – Present

**Context.** Three-party program: KT as product owner, KTDS engineering, and a partner vendor. No formal command authority over the other parties.

- **Integration contract.** Surveyed the full field set of external sources including TMDB, excluded low-signal fields (`status`, `vote_average`, `popularity`), and finalized the media agent integration specification around `contentId`, `title`, `releaseDate`, and `synopsis`.
- **Dependency reduction by design.** Adopted a structure where KTDS loads files and the media agent retrieves them by API, and assigned data quality judgment and display policy to the agent side. Neither party is bound to the other's release schedule. Cross-organization dependency is reduced more durably by architecture than by coordination cadence.
- **Constraint separation.** With no GPU allocation, self-hosted open-source inference (QWEN) was not viable; converted to API-based Gemini Flash single-path processing. Separated the cause, business-unit budget and physical hardware availability rather than a technical limit, and returned it as a documented product-owner decision item with named ownership and a response deadline. Scope, schedule, and resource trade-offs were returned to KT on the same basis.
- **Baseline scoping.** Reduced the first baseline from full-channel analysis to a single channel (SPOTV) with a phased expansion plan.
- **Program metrics.** Designed and tracks weekly: blocker age, decision lead time, and deadline-specification rate. Status narrative does not surface risk; elapsed days do.
- **Forum operation.** Ran a dual-track model for a client that resists procedural communication: conversational externally, strict decision and risk registers plus an NFR log internally. Post-meeting summary emails serve as the decision log; email threads are promoted to the system of record where Confluence is unavailable. Introduced a two-stage response protocol (immediate provisional answer, then dated confirmation) to eliminate no-response intervals.

**Results.** Media agent integration specification finalized. Contents Agent infrastructure design complete, environment build in progress. Zero blockers aged beyond 7 days.

**Stack.** Whisper (self-hosted STT), Gemini Flash API, LLM orchestration, TMDB external API, Confluence

#### KTDS Company-wide ITO Business Structure Innovation Task Force · 2024.06 – 2024.12

**Context.** Company-wide task force. Owned collection and analysis of field-level ITO contract problems.

- The difficulty was recognition, not collection: the field did not classify the situation as a problem. Scope growth without corresponding compensation had settled into accepted practice, so survey instruments returned nothing.
- Contacted team leads directly through referral, then collected, classified, and pattern-analyzed three years of new outsourcing contract cases. Once individual complaints resolved into recurring types, the matter became addressable at company level.
- Reviewed three cost estimation methodologies (expert analogy, parametric, rate-based) and performed KOSA rate-based simulation jointly with external consultants, supplying field interview data as input. Authored the consolidated findings and closing report.

**Results.** Workload measurement established as a process that continued executing for approximately 6 months after roll-off. Fed into the 2026 ITO rate increase.

#### KT Telecom Big Data Platform Portal · Portal Project Lead · 2019.07 – 2020.02

**Context.** 17 external consortium organizations, none under reporting or command authority, required to produce conforming metadata deliverables.

- Translated DCAT, an unfamiliar international metadata standard, into directly applicable form: separated 21 fields into mandatory and optional, specified authoring rules (minimum description length, title construction, keyword floor, ISO 639-1 language codes), and distributed guide, template, examples, naming conventions, and deadlines as a single package.
- Operated a two-tier communication model: asynchronous against the common guide, synchronous direct contact for non-responding organizations.
- When the standard changed mid-program from RDF to xlsx, defined an interim integration format rather than waiting for the national agency's final ruling, keeping partner work uninterrupted.
- When the lead developer, designer, and publisher all departed mid-program, personally onboarded replacements and redistributed work.

**Results.** 140 metadata records collected. Analysis, visualization, and ML linkage process designed. Launched within the ministry demonstration window with no execution gap.

**Failure and the standard that came from it.** A display-resolution mismatch in design deliverables caused rework. Receipt of design images had been treated as completion, with no defined acceptance criterion, and weekly status polling of individuals did not surface the gap between designer and publisher. The demonstration date held, but it held on added headcount. The correction was procedural, not personal: UI sizing verification was applied at Senior Care (2021) and Home Portal (2023), and test scenarios became a mandatory item in the Azure migration discovery questionnaire (2025).

#### KT AI First Contact Center (AICC) · Scenario Development Project Lead · 2020.03 – 2020.12

- The business side reframed the chatbot from inquiry handling to transaction completion. Led integration design and implementation for billing and collections core-system linkage, including failure handling and consistency conditions required for monetary transactions.
- Delivered a structure completing overdue-balance check through payment within a single conversation.

**Results.** KRW 32M collected within 3 weeks of launch.

#### Additional programs

| Period | Program | Role and outcome |
| --- | --- | --- |
| 2022.03 – 2023.02 | KT GiGA Genie backend platform | PM. Ran 3 service lines concurrently (backend, personalization, senior care) to on-schedule completion; delegated a duplicate program and assumed commercial launch directly after a colleague's departure. Proposed MicroStrategy adoption to the business analysis group and ran vendor selection and contracting. |
| 2023.10 – 2024.12 | KT Senior Care web application | PM. Led web application development, delivered within GiGA Genie TV. |
| 2021.01 – 2022.02 | KT Senior Care | PM. New service build and transition to managed operations. |
| 2018.04 – 2019.06 | KT IoT Support | SM PM. Led operations transition. Improved dashboard query performance from 200s to 1s (company incentive award). Restructured NB-IoT monitoring screens, reducing CPU and memory utilization. |

### R&B Software · Developer and Operations · 2009.01 – 2014.12

Siebel CRM operations and development for KT sales systems. Built approximately 50 to 60 order-to-legacy integration interfaces under Agile sprint delivery. Designed and implemented campaign assignment rules. Module lead for the B2C CRM marketing module during the next-generation sales system program (Siebel to Nexacro), delivering soft launch and production launch; received CEO commendation.

---

## AI IN PROGRAM MANAGEMENT

- **Delivery workflow.** AI-assisted log analysis to narrow root-cause hypotheses and reduce investigation time (Azure StatefulSet failure, 2025).
- **Architecture judgment.** Finalized the Whisper STT to Contents Agent orchestration to Gemini Flash cascade pipeline with the engineering team, deciding the self-hosted versus API trade-off under a hard resource constraint.
- **Formal training.** Agentic AI program completed 2026.06 (LangChain, LangGraph, RAG, MCP, multi-agent). CLI-based agent development environments configured on work and personal machines, including corporate proxy and TLS inspection resolution.
- **Prototyping.** Receipt-to-expense-log chatbot POC on Azure AI Foundry and Azure OpenAI (Vision API extraction to weekly summary).
- **Automation attempt, halted.** Weekly-report summarization via Confluence and Rovo AI into Teams; stopped at permission and platform availability constraints. Recorded rather than dropped.
- **AWS Summit Seoul 2025**, agentic AI data pipeline session (ReAct loops, MCP, agent memory, data governance).

---

## TECHNICAL PROFILE

| Area | Detail |
| --- | --- |
| Cloud and infrastructure | Azure, Kubernetes (AKS), Rancher, Kustomize, ArgoCD, Microsoft Entra ID, Azure Landing Zone, Application Gateway, Microsoft Defender for Cloud |
| Data | SQL (PostgreSQL, MySQL, MariaDB), query performance tuning, MicroStrategy (BI) adoption and vendor selection, metric design and weekly tracking |
| AI | Whisper (STT), Gemini API, LLM orchestration, Azure AI Foundry / Azure OpenAI, AI-assisted log analysis |
| Program management | Structured discovery interviews, integration specification ownership, architecture decision forums, risk and decision registers, NFR logging, milestone and dependency management |
| Tooling | Jira, Confluence |
| Development background | Java/JSP, Siebel CRM, Nexacro |

---

## CERTIFICATIONS AND EDUCATION

| Item | Detail |
| --- | --- |
| Certifications | Certified Kubernetes Administrator, CKA (2026.01) · AWS Solutions Architect Associate (2024.05) · Siebel 8 Consultant Expert (2011) · Engineer Information Processing, KR national certification (2009) |
| Committed within onboarding | PMP and Databricks Certified Associate, both scheduled within the 6-month requirement stated in the role description |
| Education | B.S. Computer Science, Hanshin University (2009.02) |

---

## LANGUAGES

- **Korean.** Native.
- **English.** Currently studying; working toward professional proficiency in written and spoken English.
