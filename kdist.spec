%define _libexecdir /usr/libexec

Summary:	Tool for managing Mandriva kernel builds
Name:		kdist
Version:	0.0.4
Release:	%mkrel 1
License: 	GPL v2
Group: 		System/Configuration/Hardware
Source0:	%{name}-%{version}.tar.bz2
URL:		http://git.mandriva.com/projects/?p=users/fbui/kdist.git
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
