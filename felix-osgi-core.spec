%global pkg_name felix-osgi-core
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global bundle org.osgi.core

Name:    %{?scl_prefix}%{pkg_name}
Version: 1.4.0
Release: 15.9%{?dist}
Summary: Felix OSGi R4 Core Bundle

License: ASL 2.0
URL:     http://felix.apache.org/site/apache-felix-osgi-core.html
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}felix-parent
BuildRequires: %{?scl_prefix}maven-surefire-provider-junit
BuildRequires: %{?scl_prefix_java_common}javapackages-tools

%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{bundle}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x

%mvn_alias :%{bundle} org.osgi:%{bundle}
%mvn_file :%{bundle} felix/%{bundle}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.4.0-15.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.4.0-15.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-15.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-15.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-15.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-15.4
- Remove requires on java

* Fri Feb 14 2014 Michael Simacek <msimacek@redhat.com> - 1.4.0-15.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-15.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-15.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4.0-15
- Mass rebuild 2013-12-27

* Fri Aug 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-14
- Migrate away from mvn-rpmbuild (#997435)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-13
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Feb 25 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-12
- Add missing BR: maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Jaromir Capik <jcapik@redhat.com> 1.4.0-8
- Extra groupId "org.osgi" added
- Minor spec file changes according to the latest guidelines
- fixing "unmappable character for encoding ANSI_X3.4-1968"

* Wed Mar 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4.0-7
- Build with maven 3 and drop ant buil.xml files.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-5
- Remove felix-parent from Requires to prevent pulling maven in

* Tue Dec 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-4
- Add felix-parent to Requires (maven builds require this)
- Add license and jpackage-utils Requires to javadoc subpackage
- Use mavenpomdir macro

* Mon Dec 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.4.0-3
- Fix pom name.
- Adapt to current guidelines.

* Tue Jun 29 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.4.0-2
- Modify maven-build.xml to include MANIFEST.MF into JAR

* Tue Jun 22 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.4.0-1
- Update felix-osgi-core-1.4.0-build.xml.tar.gz
- Use the macros style
- Release 1.4.0

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-2
- Fix line length.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-1
- Initial package.
