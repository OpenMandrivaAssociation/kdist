%define _libexecdir /usr/libexec

Summary:	Tool for managing Mandriva kernel builds
Name:		kdist
Version:	0.0.4
Release:	2
License: 	GPL v2
Group: 		System/Configuration/Hardware
Source0:	%{name}-%{version}.tar.bz2
URL:		https://git.mandriva.com/projects/?p=users/fbui/kdist.git
BuildRoot: 	%{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch

%description
Kdist is a tool for managing Mandriva kernel builds from a git repository.

%prep
%setup -q

%build

%install
%makeinstall_std prefix=/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755, root, root) %_bindir/kdist
%_libexecdir/kdist/


%changelog
* Tue Jul 26 2011 Franck Bui <franck.bui@mandriva.com> 0.0.4-1mdv2012.0
+ Revision: 691729
- v0.0.4
- Upgrade to v0.0.2

* Mon Jun 27 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.0.1-1
+ Revision: 687561
- Imported kdist
- Created package structure for kdist.

