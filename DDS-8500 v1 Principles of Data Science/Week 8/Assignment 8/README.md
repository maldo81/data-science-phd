# InsightsCG Health - Documentation Index

**Last Updated**: 2025-10-19
**System Version**: 1.0
**Status**: ✅ Production-Ready (85% Complete)

---

## 📚 Documentation Hub

Welcome to the InsightsCG Health documentation. This is a comprehensive Healthcare Information Exchange platform combining **Multi-Stakeholder EMR** (38+ portals, 95 roles) with **AI-Powered Personal Health** features (meal planning, glucose pattern detection) and **External Partner APIs** (FHIR R4, OAuth 2.0).

### 🎯 Quick Links

- **📊 What's Ready?** → [System Status](11-current-status/SYSTEM_STATUS.md) ⭐ **START HERE**
- **📱 What Can It Do?** → [Companion App Documentation](10-apps/companion/README.md) ⭐ **COMPREHENSIVE**
- **🎯 Marketing Materials** → [Marketing Documentation](12-marketing/) ⭐ **NEW**
- **🔑 Demo Accounts** → [Demo Accounts](../DEMO_ACCOUNTS.md) (47 test accounts)
- **🏗️ Architecture** → [Architecture](01-architecture/)
- **⚡ Features** → [Features](02-features/)
- **🚀 Deployment** → [Deployment](03-deployment/)
- **🧪 Testing** → [Testing Guide](04-testing/TESTING_GUIDE.md)
- **🔌 Partner APIs** → [API Reference](06-api-reference/)
- **🤝 Integration** → [Integration Guides](07-integration-guides/)
- **👥 User Guides** → [User Guides](08-user-guides/)

---

## 📖 Documentation Structure

### 1️⃣ Architecture & Design

Understanding the system design and technical architecture.

- **[System Overview](01-architecture/system-overview.md)** - High-level architecture, tech stack, design principles
- **[Database Schema](01-architecture/database-schema.md)** - ER diagrams, table descriptions, relationships
- **[API Architecture](01-architecture/api-architecture.md)** - FHIR R4 compliance, REST patterns, authentication
- **[Security Architecture](01-architecture/security-architecture.md)** - HIPAA compliance, encryption, audit logging

### 2️⃣ Features & Capabilities

Detailed documentation for each feature with implementation details and testing.

#### Core Health & Nutrition Platform (Pre-EMR)
- **[Health Monitoring](02-features/health-monitoring.md)** - Vitals tracking, glucose monitoring, medication management
- **[Meal Planning & Nutrition](02-features/meal-planning.md)** - AI-powered meal plans, recipe management, grocery lists
- **[Conversational AI Assistant](02-features/ai-assistant.md)** - Chat interface, RAG, real-time guidance

#### Hospital EMR System (Phases 1-7)
- **[Hospital EMR Core](02-features/hospital-emr.md)** - Encounters, appointments, practitioners, SOAP notes
- **[Multi-Stakeholder APIs](02-features/multi-stakeholder-apis.md)** - Lab, pharmacy, insurance integrations (FHIR R4)
- **[Ministry of Health Analytics](02-features/moh-analytics.md)** - Population health reporting, disease surveillance
- **[Clinical Decision Support](02-features/clinical-decision-support.md)** - Drug interactions, allergy alerts, critical labs
- **[Medical Imaging](02-features/medical-imaging.md)** - PACS integration, radiology reports, DICOM studies
- **[Care Coordination](02-features/care-coordination.md)** - Care teams, care plans, referrals, clinical pathways
- **[Patient Portal](02-features/patient-portal.md)** - Patient self-service, messaging, appointments, documents
- **[Multi-Facility Support](02-features/multi-facility.md)** - Organization hierarchy, cross-facility access
- **[Analytics & Reporting](02-features/analytics-reporting.md)** - Population cohorts, quality measures, dashboards
- **[Multi-Factor Authentication](02-features/mfa-security.md)** - TOTP MFA, backup codes, password policies

### 3️⃣ Deployment & Configuration

Getting the system running in different environments.

- **[Local Development Setup](03-deployment/local-development.md)** - Prerequisites, installation, running locally
- **[Docker Deployment](03-deployment/docker-deployment.md)** - Docker, docker-compose, container orchestration
- **[Kubernetes Deployment](03-deployment/kubernetes-deployment.md)** - K8s manifests, scaling, production configuration
- **[Production Hardening](03-deployment/production-hardening.md)** - Security checklist, monitoring, performance tuning
- **[Backup & Recovery](03-deployment/backup-recovery.md)** - Automated backups, disaster recovery procedures

### 4️⃣ Testing & Quality Assurance

Ensuring system reliability and correctness.

- **[Testing Guide](04-testing/testing-guide.md)** - Comprehensive testing strategy, test coverage
- **[API Testing](04-testing/api-testing.md)** - Postman collections, curl examples, integration tests
- **[Load Testing](04-testing/load-testing.md)** - Locust setup, performance benchmarks
- **[Security Testing](04-testing/security-testing.md)** - Vulnerability scanning, penetration testing

### 5️⃣ Operations & Maintenance

Running and maintaining the system in production.

- **[Monitoring](05-operations/monitoring.md)** - Sentry, Prometheus, Grafana dashboards
- **[Troubleshooting](05-operations/troubleshooting.md)** - Common issues, error messages, solutions
- **[Maintenance](05-operations/maintenance.md)** - Daily/weekly/monthly operational tasks
- **[Incident Response](05-operations/incident-response.md)** - On-call procedures, escalation paths

### 6️⃣ API Reference

Complete API documentation with examples.

- **[FHIR API](06-api-reference/fhir-api.md)** - Lab, pharmacy, insurance endpoints (FHIR R4)
- **[Clinical Decision Support API](06-api-reference/clinical-support-api.md)** - Interaction checking, alerts
- **[Medical Imaging API](06-api-reference/imaging-api.md)** - Imaging orders, studies, reports
- **[Analytics API](06-api-reference/analytics-api.md)** - Cohorts, quality measures, dashboards
- **[MFA API](06-api-reference/mfa-api.md)** - MFA enrollment, verification, management
- **[MOH API](06-api-reference/moh-api.md)** - Ministry of Health reporting endpoints
- **[Swagger UI](06-api-reference/swagger-ui.md)** - Interactive API documentation

### 7️⃣ Integration Guides

Partner integration guides for external stakeholders (labs, pharmacies, insurance).

- **[Lab Partner Integration](07-integration-guides/lab-partners.md)** - OAuth setup, FHIR ServiceRequest/DiagnosticReport
- **[Pharmacy Partner Integration](07-integration-guides/pharmacy-partners.md)** - MedicationRequest/MedicationDispense workflow
- **[Insurance Provider Integration](07-integration-guides/insurance-providers.md)** - Claims processing, pre-authorization
- **[Ministry of Health Analytics](07-integration-guides/moh-analytics.md)** - Population health reporting API

### 8️⃣ User Guides

End-user documentation and quick-start guides.

- **[AI Clinical Assistant](08-user-guides/ai-clinical-assistant.md)** - Using the conversational AI for patient guidance
- **[Quick Reference](08-user-guides/quick-reference.md)** - Common commands and quick lookups
- **[Spanish Pages Guide](08-user-guides/spanish-pages.md)** - Managing bilingual content
- **[Document Extraction Quickstart](08-user-guides/document-extraction-quickstart.md)** - Uploading and processing medical documents
- **[Meal Planning User Guide](08-user-guides/user_guide_meal_planning.md)** - Planning meals and managing nutrition
- **[Meal Plan Components](08-user-guides/meal_plan_components.md)** - Understanding multi-component meal structure

### 9️⃣ Roadmap & Strategic Planning

Product roadmap and strategic planning documents.

- **[Consolidated Roadmap](09-roadmap/consolidated-roadmap.md)** - ⭐ **START HERE** - Unified strategic roadmap (B2C + B2B/EMR)
- **[Development Roadmap](09-roadmap/DEVELOPMENT_ROADMAP.md)** - B2C personal health features roadmap
- **[Strategic Roadmap](09-roadmap/STRATEGIC_ROADMAP.md)** - Multi-stakeholder EMR strategy
- **[3-Week Hospital Pilot Roadmap](09-roadmap/3_WEEK_ROADMAP.md)** - Hospital pilot implementation plan
- **[Clinician Dashboard Plan](09-roadmap/clinician_dashboard_plan.md)** - Clinician portal specifications
- **[EMR Multi-Stakeholder Architecture](09-roadmap/EMR_MULTI_STAKEHOLDER_ARCHITECTURE.md)** - Comprehensive EMR architecture

---

## 🚀 Getting Started

### For Developers

1. **Read**: [System Overview](01-architecture/system-overview.md) to understand the architecture
2. **Setup**: Follow [Local Development](03-deployment/local-development.md) to get running
3. **Explore**: Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for common commands
4. **Test**: Use [Testing Guide](04-testing/testing-guide.md) to verify your setup

### For DevOps Engineers

1. **Review**: [Security Architecture](01-architecture/security-architecture.md) for compliance
2. **Deploy**: Use [Docker Deployment](03-deployment/docker-deployment.md) or [Kubernetes](03-deployment/kubernetes-deployment.md)
3. **Harden**: Follow [Production Hardening](03-deployment/production-hardening.md) checklist
4. **Monitor**: Set up [Monitoring](05-operations/monitoring.md) and [Incident Response](05-operations/incident-response.md)

### For QA Engineers

1. **Understand**: [Testing Guide](04-testing/testing-guide.md) for testing strategy
2. **Manual Tests**: [API Testing](04-testing/api-testing.md) for endpoint verification
3. **Load Tests**: [Load Testing](04-testing/load-testing.md) for performance validation
4. **Security**: [Security Testing](04-testing/security-testing.md) for vulnerability checks

### For Product Managers

1. **Strategy**: Start with [Consolidated Roadmap](09-roadmap/consolidated-roadmap.md) for product vision
2. **Features**: Browse [Features](02-features/) to understand capabilities
3. **Integration**: Review [Integration Guides](07-integration-guides/) for partner integrations
4. **Analytics**: Check [Analytics & Reporting](02-features/analytics-reporting.md) for insights
5. **Portal**: See [Patient Portal](02-features/patient-portal.md) for patient-facing features

### For External Partners (Labs, Pharmacies, Insurance)

1. **Start Here**: Review [Integration Guides](07-integration-guides/) for your stakeholder type
2. **API Access**: Check [FHIR API](06-api-reference/fhir-api.md) for technical specifications
3. **Testing**: Use [API Testing](04-testing/api-testing.md) to verify integration
4. **Support**: Contact integration support for credentials and assistance

---

## 📊 System Statistics

| Metric | Count |
|--------|-------|
| **Phases Completed** | 7 (100%) |
| **API Endpoints** | 71 |
| **Database Tables** | 36 |
| **Migrations** | 46 |
| **FHIR Resources** | 15+ |
| **Security Features** | MFA, Encryption, Audit Logging |
| **Test Coverage** | 85%+ |
| **Uptime Target** | 99.9% |

---

## 🏥 System Capabilities

### Core Health Management (Original App)
- ✅ Vitals tracking (glucose, BP, heart rate)
- ✅ Medication management with reminders
- ✅ Lab results viewing
- ✅ AI-powered meal planning
- ✅ Recipe management with nutrition info
- ✅ Grocery list generation
- ✅ CGM integration (Dexcom)
- ✅ Conversational AI assistant

### Hospital EMR (Phases 1-7)
- ✅ Complete EMR (encounters, SOAP notes, appointments)
- ✅ Multi-stakeholder integrations (labs, pharmacies, insurance)
- ✅ FHIR R4 compliance
- ✅ Clinical decision support (drug interactions, alerts)
- ✅ Medical imaging (PACS, radiology reports)
- ✅ Care coordination (teams, plans, referrals)
- ✅ Patient portal (self-service, messaging)
- ✅ Multi-facility support
- ✅ Population health analytics
- ✅ Quality measure tracking (HEDIS, CMS)
- ✅ Multi-factor authentication
- ✅ HIPAA compliance
- ✅ Production-ready infrastructure

---

## 🔐 Security & Compliance

### HIPAA Compliance
- ✅ **Access Controls**: MFA, role-based access, session timeout
- ✅ **Audit Controls**: PHI access logging, 7-year retention
- ✅ **Integrity Controls**: Data validation, checksums
- ✅ **Transmission Security**: TLS 1.3, end-to-end encryption
- ✅ **Administrative**: Security policies, incident response
- ✅ **Physical**: Cloud provider compliance (AWS/GCP)
- ✅ **Technical**: Encryption at rest, field-level encryption

### Security Features
- ✅ Multi-factor authentication (TOTP)
- ✅ Password policies (complexity, history, expiration)
- ✅ API rate limiting (DRF throttling)
- ✅ Field-level encryption (SSN, credit cards)
- ✅ Session idle timeout (15 minutes)
- ✅ Brute-force protection (account lockout)
- ✅ Security scanning (Bandit, Safety)

---

## 🌍 Technology Stack

### Backend
- **Framework**: Django 4.2, Django REST Framework
- **Language**: Python 3.12
- **Database**: PostgreSQL 14 + pgvector
- **Cache**: Redis 7.0
- **Task Queue**: Celery
- **Real-time**: Django Channels (WebSocket)

### Standards Compliance
- **Healthcare**: FHIR R4, HL7 v2.5, DICOM
- **Security**: HIPAA, SOC 2
- **Quality**: HEDIS, CMS Star Ratings, MIPS

### Infrastructure
- **Containers**: Docker, Kubernetes
- **CI/CD**: GitHub Actions
- **Cloud**: AWS (EC2, RDS, S3, ElastiCache)
- **Monitoring**: Sentry, Prometheus, Grafana

---

## 📞 Support & Resources

### Documentation
- **Main Docs**: You're here! Browse folders above
- **Roadmap**: [Consolidated Roadmap](09-roadmap/consolidated-roadmap.md) - Strategic planning and vision
- **Quick Reference**: [Quick Reference Guide](08-user-guides/quick-reference.md)
- **User Guides**: [User Guides](08-user-guides/) - End-user documentation
- **Integration**: [Integration Guides](07-integration-guides/) - Partner integration docs
- **API Docs**: http://localhost:8000/api/docs/ (Swagger UI)

### External Resources
- **FHIR Specification**: https://www.hl7.org/fhir/
- **Django Docs**: https://docs.djangoproject.com/
- **HIPAA Guidelines**: https://www.hhs.gov/hipaa/
- **Kubernetes Docs**: https://kubernetes.io/docs/

### Getting Help
- **Issues**: GitHub Issues
- **Email**: support@healthapp.example.com
- **Emergency**: PagerDuty on-call

---

## 🗂️ Archive

Historical documentation from development phases has been moved to [archive/](archive/):

- **[archive/progress-notes/](archive/progress-notes/)** - Development progress notes, session summaries, status updates
- **[archive/guides/](archive/guides/)** - Legacy implementation guides, superseded by comprehensive feature docs

These docs are kept for historical reference but may be outdated. Always refer to the main documentation structure above for current information.

---

## 📝 Contributing to Documentation

When updating docs:

1. **Keep feature docs self-contained** - Include overview, implementation, and testing
2. **Update cross-references** - When moving/renaming files, update links
3. **Include code examples** - Show working curl commands and code snippets
4. **Add testing sections** - Every feature should have testing instructions
5. **Update this README** - Add new docs to the appropriate section

---

**Status**: ✅ **All 7 Phases Complete - Production Ready**

**Last Updated**: October 2025
**Documentation Version**: 1.0
**System Version**: 1.0.0
